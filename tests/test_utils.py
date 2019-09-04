from pathlib import Path

import pytest
from video_tools.utils import (
    filter_compressible_files,
    generate_output_file,
    is_meta_file,
    is_processed_file,
    is_video_file,
)


@pytest.mark.parametrize(
    "input_name, output_name",
    [
        ("a.mp4", "a_compressed.mp4"),
        ("/tmp/asd.mov", "/tmp/asd_compressed.mp4"),
        ("c:/someFolder/asd.wmv", "c:/someFolder/asd_compressed.mp4"),
    ],
)
def test_generate_output_file(input_name, output_name):
    file_ = Path(input_name)
    output_file = generate_output_file(file_)
    assert str(output_file) == output_name


@pytest.mark.parametrize(
    "input_name, expected",
    [
        ("a.mp4", False),
        ("a_compressed.mp4", True),
        ("c:/someFolder/asd.wmv", False),
        ("c:/someFolder/asd_compressed.mp4", True),
    ],
)
def test_is_processed_file(input_name, expected):
    file_ = Path(input_name)
    result = is_processed_file(file_)
    assert result is expected


@pytest.mark.parametrize(
    "input_name, expected",
    [
        ("a.mp4", True),
        ("a_compressed.mp4", True),
        ("aa.mov", True),
        ("b.txt", False),
        ("c.py", False),
    ],
)
def test_is_video_file(input_name, expected):
    file_ = Path(input_name)
    result = is_video_file(file_)
    assert result is expected


@pytest.mark.parametrize(
    "input_name, expected",
    [
        ("a.mp4", False),
        ("._a.mp4", True),
        ("c:/someFolder/asd.wmv", False),
        ("c:/someFolder/._asd.wmv", True),
    ],
)
def test_is_meta_file(input_name, expected):
    file_ = Path(input_name)
    result = is_meta_file(file_)
    assert result is expected


def test_filter_compressible_files():
    files = [
        Path("a.mp4"),
        Path("a_compressed.mp4"),
        Path("._a.mp4"),
        Path("aa.mov"),
        Path("b.txt"),
    ]
    expected = [Path("a.mp4"), Path("aa.mov")]
    result = list(filter_compressible_files(files))
    assert result == expected
