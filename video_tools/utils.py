import subprocess

import click

from .constants import IGNORED_PATTERNS, OUTPUT_SUFFIX, SUPPORTED_EXTENSIONS


def is_video_file(file_):
    for extension in SUPPORTED_EXTENSIONS:
        if file_.match(f"*.{extension}"):
            return True
    return False


def is_meta_file(file_):
    for pattern in IGNORED_PATTERNS:
        if file_.match(pattern):
            return True
    return False


def is_processed_file(file_):
    return file_.match(f"*{OUTPUT_SUFFIX}")


def filter_compressable_files(files):
    for file_ in files:
        if (
            is_video_file(file_)
            and not is_processed_file(file_)
            and not is_meta_file(file_)
        ):
            yield file_


def generate_output_file(in_file):
    return in_file.with_name(in_file.stem + OUTPUT_SUFFIX)


def call_ffmpeg(in_file, out_file):
    # fmt: off
    subprocess.run(
        [
            "ffmpeg",
            "-i", str(in_file),
            "-c:v", "libx265", "-crf", "28",
            "-c:a", "aac", "-b:a", "128k",
            str(out_file),
        ],
        check=True,
    )
    # fmt: on


def delete_file(file_):
    print_style(f"Deleting: {file_}", fg="red")
    file_.unlink()


def print_style(msg, **kwargs):
    kwargs.setdefault("fg", "green")
    click.echo(click.style(msg, **kwargs))
