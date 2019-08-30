import os
import subprocess

import click

from .constants import IGNORED_PATTERNS, OUTPUT_SUFFIX, SUPPORTED_EXTENSIONS


def is_video_file(file_):
    for pattern in SUPPORTED_EXTENSIONS:
        if file_.name.endswith(pattern):
            return True
    return False


def is_meta_file(file_):
    for pattern in IGNORED_PATTERNS:
        if file_.name.startswith(pattern):
            return True
    return False


def is_processed_file(file_):
    return file_.name.endswith(OUTPUT_SUFFIX)


def call_ffmpeg(file_):
    in_filename = str(file_)
    out_filename = "{}{}".format(in_filename[:-4], OUTPUT_SUFFIX)
    subprocess.run(
        [
            "ffmpeg",
            "-i", in_filename,
            "-c:v", "libx265", "-crf", "28",
            "-c:a", "aac", "-b:a", "128k",
            out_filename,
        ],
        check=True,
    )


def delete_file(file_):
    filename = str(file_)
    click.echo(click.style('Deleting: {}'.format(filename), fg='red'))
    os.remove(filename)
