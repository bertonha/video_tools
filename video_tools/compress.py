from pathlib import Path

import click

from .utils import (
    call_ffmpeg,
    delete_file,
    is_meta_file,
    is_processed_file,
    is_video_file,
)


def compress_file(file_, delete):
    if (
        not is_video_file(file_)
        or is_processed_file(file_)
        or is_meta_file(file_)
    ):
        return
    try:
        call_ffmpeg(file_)
    except Exception:
        return
    if delete:
        delete_file(file_)


@click.group()
def compress_group():
    pass


@compress_group.command()
@click.option("--delete", default=False, is_flag=True)
@click.argument("initial_path")
def compress(initial_path, delete):
    p = Path(initial_path)

    if p.is_dir():
        files = p.glob("**/*")
    else:
        files = [p]

    for file_ in files:
        compress_file(file_, delete)
