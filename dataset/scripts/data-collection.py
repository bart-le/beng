import argparse
import datetime
import math
import os
import sys
import time

import cv2
from mediapipe.python.solutions import drawing_styles, drawing_utils, hands


def countdown_before_recording(
    capture: cv2.VideoCapture, countdown: float, pose_estimation: bool
) -> None:
    """
    Displays a countdown timer along with MediaPipe pose keypoints before starting to record.

    Args:
        capture (cv2.VideoCapture): VideoCapture object from cv2 to capture video frames.
        countdown (float): Countdown time before recording in seconds.
        pose_estimation (bool): If true, MediaPipe hand skeletal poses are displayed each frame.
    """
    end_time = time.time() + countdown

    with hands.Hands(
        min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1
    ) as estimator:
        while countdown > 0:
            _, frame = capture.read()

            if pose_estimation:
                frame.flags.writeable = False
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                results = estimator.process(frame)

                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        drawing_utils.draw_landmarks(
                            frame,
                            hand_landmarks,
                            hands.HAND_CONNECTIONS,
                            drawing_styles.get_default_hand_landmarks_style(),
                            drawing_styles.get_default_hand_connections_style(),
                        )

            font_scale = 10
            thickness = 10
            text = str(f"{countdown:.1f}")
            text_size, _ = cv2.getTextSize(
                text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness
            )

            x = int((frame.shape[1] - text_size[0]) / 2)
            y = int((frame.shape[0] + text_size[1]) / 2)

            frame = cv2.flip(frame, 1)

            frame = cv2.putText(
                img=frame,
                text=text,
                org=(x, y),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=font_scale,
                color=(0, 0, 255),
                thickness=thickness,
            )

            countdown = end_time - time.time()

            cv2.imshow("Recording", frame)
            cv2.waitKey(1)


def record_video(capture: cv2.VideoCapture, eta: str, path: str, label: str) -> None:
    """
    Records a video with the specified label and person_id.
    Inserts a delay before starting the recording if delay is True.
    Displays a progress bar and frame count during recording.

    Args:
        capture (cv2.VideoCapture): VideoCapture object from cv2 to capture video frames.
        eta (str): Estimated time until the end of the recording session.
        path (str): Output directory to save recordings.
        label (str): Label to be used for the video.
    """
    video_number = get_next_video_number(path, label)
    video_filename = f"{label}/{label}-{video_number:03}.mp4"
    video_path = os.path.join(path, video_filename)

    fps = 30
    num_frames = fps * 2
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(video_path, codec, fps, (1280, 720))

    frame_count = 0

    while frame_count < num_frames:
        _, frame = capture.read()
        video_writer.write(frame)

        frame = cv2.flip(frame, 1)

        progress = frame_count / num_frames
        bar_width = int(progress * 1280)

        if progress <= 0.5:
            color = (int(255 * (1 - progress * 2)), 255, 255)
        else:
            color = (0, int(255 * (1 - (progress - 0.5) * 2)), 255)

        cv2.rectangle(
            img=frame, pt1=(0, 700), pt2=(bar_width, 720), color=color, thickness=-1
        )

        frame = cv2.putText(
            img=frame,
            text=str(f"{frame_count + 1:02}/60 | {eta} | {video_number:03}"),
            org=(10, 30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=(0, 0, 255),
            thickness=2,
        )

        cv2.imshow("Recording", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        frame_count += 1

    video_writer.release()
    print(f'Video saved at "{video_path}".', end="\r", flush=True)


def get_next_video_number(path: str, label: str) -> int:
    """
    Returns the next video number for the specified label.

    Args:
        path (str): Output directory to save recordings.
        label (str): Label used for the video.

    Returns:
        int: The next video number.
    """
    label_directory = os.path.join(path, label)

    os.makedirs(label_directory, exist_ok=True)

    existing_videos = [
        filename
        for filename in os.listdir(label_directory)
        if filename.startswith(f"{label}-")
    ]

    return len(existing_videos)


def parse_args() -> argparse.Namespace:
    """
    This is a function that parses arguments from command line.

    Returns:
        argparse.Namespace: The populated namespace.
    """

    parser = argparse.ArgumentParser(description="Hand landmark data collection.")

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        required=True,
        help="output path",
    )
    parser.add_argument(
        "-l",
        "--label",
        type=str,
        required=True,
        help="Polish Sign Language alphabet letter",
    )
    parser.add_argument(
        "-t",
        "--total",
        type=int,
        default=1000,
        help="total number of recordings",
    )
    parser.add_argument(
        "-b",
        "--batch",
        type=int,
        default=100,
        help="fraction of recording batches between countdowns",
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=float,
        default=0,
        help="delay time before each recording",
    )
    parser.add_argument(
        "-c",
        "--countdown",
        type=int,
        default=10,
        help="countdown time between recording batches",
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    """
    Records videos based on command-line arguments.

    Args:
        args (argparse.Namespace): The command-line arguments.
    """
    path = args.path
    label = args.label
    total = args.total
    batch = args.batch
    delay = args.delay
    countdown = args.countdown

    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    for i in range(total):
        recordings_left = total - i

        recording_time = recordings_left * 2

        if delay > 0:
            recording_time = recording_time + (recordings_left * delay)

        recording_time += (recordings_left // batch) * countdown

        eta = str(datetime.timedelta(seconds=math.ceil(recording_time)))

        new_batch = i % batch == 0

        if new_batch:
            countdown_before_recording(capture, countdown, True)

        if delay > 0:
            countdown_before_recording(capture, delay, False)

        record_video(capture, eta, path, label.upper())

    capture.release()


if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        sys.exit(130)
