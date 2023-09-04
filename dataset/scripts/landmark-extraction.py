import argparse
import os
import sys
from typing import NamedTuple

import cv2
import pandas as pd
from mediapipe.python.solutions import hands

keypoints = [keypoint.name for keypoint in hands.HandLandmark]
columns = [f"{keypoint}_{axis}" for keypoint in keypoints for axis in ["x", "y", "z"]]


def detect_right_hand(multi_hand_landmarks: NamedTuple) -> int:
    """
    Detects right hand by comparing furthest wrist points of a mirrored video.

    Args:
        multi_hand_landmarks (NamedTuple): Normalised hand landmarks.

    Returns:
        int: Right hand index.
    """
    right_hand_index = 0

    if multi_hand_landmarks:
        right_hand = multi_hand_landmarks[right_hand_index]
        right_hand_x = right_hand.landmark[hands.HandLandmark.WRIST].x

        for hand_index, hand in enumerate(multi_hand_landmarks):
            if hand.landmark[hands.HandLandmark.WRIST].x >= right_hand_x:
                right_hand_index = hand_index
    return right_hand_index


def extract_landmarks(input_path: str, output_path: str) -> None:
    """
    Extracts right hand landmark keypoints from every frame and saves it to a CSV file.

    Args:
        input_path (str): Video source input path.
        output_path (int): Output path of the file to be saved.
    """
    cap = cv2.VideoCapture(input_path)

    frames = []

    while cap.isOpened():
        with hands.Hands(
            model_complexity=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            max_num_hands=2,
        ) as estimator:
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = estimator.process(frame)
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            multi_hand_landmarks = results.multi_hand_landmarks
            multi_hand_world_landmarks = results.multi_hand_world_landmarks

            right_hand_index = detect_right_hand(multi_hand_landmarks)

            if multi_hand_world_landmarks:
                right_hand = multi_hand_world_landmarks[right_hand_index]
                frame = []

                for keypoint in right_hand.landmark:
                    frame.extend([keypoint.x, keypoint.y, keypoint.z])

                frames.append(frame)

    cap.release()

    df = pd.DataFrame(data=frames, columns=columns)

    df.to_csv(output_path)

    print(f'Tabular data saved at "{output_path}".', end="\r", flush=True)


def parse_args():
    """
    This is a function that parses arguments from command line.

    Returns:
        argparse.Namespace: The populated namespace.
    """

    parser = argparse.ArgumentParser(description="Hand landmark data extractor.")

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        required=True,
        help="path to the video dataset",
    )
    parser.add_argument(
        "-l",
        "--letters",
        nargs="+",
        required=True,
        type=str,
        help="letters",
    )

    return parser.parse_args()


def main(args) -> None:
    """
    Extracts keypoints from videos frames based on command-line arguments.

    Args:
        args (argparse.Namespace): The command-line arguments.
    """
    input_directory = args.path
    letters = args.letters

    for root, _, files in os.walk(input_directory):
        if root is input_directory:
            continue

        label = os.path.basename(root)

        if label in letters:
            output_subdirectory = root.replace("video", "tabular")

            if not os.path.exists(output_subdirectory):
                os.makedirs(output_subdirectory)

            for file in files:
                name = os.path.splitext(file)[0]

                input_path = f"{root}/{file}"
                output_path = f"{output_subdirectory}/{name}.csv"

                if not os.path.exists(output_path):
                    extract_landmarks(input_path, output_path)


if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        sys.exit(130)
