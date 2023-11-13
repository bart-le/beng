import argparse
import os
import sys
from typing import List, Tuple

import pandas as pd
from mediapipe.python.solutions import hands

keypoints = [keypoint.name for keypoint in hands.HandLandmark]
columns = [
    "SIGN",
    "STATIC",
    "SAMPLE",
    "FRAME",
    *(f"{keypoint}_{axis}" for keypoint in keypoints for axis in ["X", "Y", "Z"]),
]
alphabet = [
    "A",
    "Ą",
    "B",
    "C",
    "Ć",
    "CH",
    "CZ",
    "D",
    "E",
    "Ę",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "Ł",
    "M",
    "N",
    "Ń",
    "O",
    "Ó",
    "P",
    "R",
    "RZ",
    "S",
    "Ś",
    "SZ",
    "T",
    "U",
    "W",
    "Y",
    "Z",
    "Ź",
    "Ż",
]
static = [
    "A",
    "B",
    "C",
    "E",
    "I",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "S",
    "T",
    "U",
    "W",
    "Y",
]


def get_name(file_path: str) -> Tuple[str, int]:
    """
    Splits file path into sign label and sample index.

    Args:
        file_path (str): Table path.

    Returns:
        Tuple[str, int]: Polish Sign Language alphabet letter and sample index.
    """
    base = os.path.basename(file_path)
    name = os.path.splitext(base)[0]
    sign, index = name.split("-")

    return sign, int(index)


def polish_sort_key(file_path: str) -> Tuple[int, int]:
    """
    Returns the sort key as label and sample indices.

    Args:
        file_path (str): Table path.

    Returns:
        Tuple[int, int]: Label index in the Polish Sign Language alphabet and the sample index.
    """
    sign, index = get_name(file_path)

    return alphabet.index(sign), index


def get_sorted_files(input_directory: str) -> List[str]:
    """
    Sorts file paths by alphabetical order.

    Args:
        input_directory (str): Input directory path.

    Returns:
        List[str]: Sorted file paths.
    """
    paths = []

    for root, _, files in os.walk(input_directory):
        if root is input_directory:
            continue

        paths = [*paths, *(f"{root}/{file}" for file in files)]

    return sorted(paths, key=polish_sort_key)


def parse_args() -> argparse.Namespace:
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

    return parser.parse_args()


def main(args) -> None:
    """
    Merges dataset into a single CSV file.

    Args:
        args (argparse.Namespace): The command-line arguments.
    """
    input_directory = f"{os.path.normpath(args.path)}"
    output_path = f"{input_directory}.csv"

    paths = get_sorted_files(input_directory)

    frames = []

    for path in paths:
        df = pd.read_csv(path, index_col=0)

        sign, sample = get_name(path)

        for index, row in df.iterrows():
            frames.append([sign, sign in static, sample, index, *row.values])

    chunked = pd.DataFrame(data=frames, columns=columns)

    chunked.to_csv(output_path, index=False)


if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        sys.exit(130)
