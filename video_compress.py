import os
import subprocess

import click
from pathlib import Path


OUTPUT_SUFFIX = "_compressed.mp4"

EXTENSION_LIST = [
    "mp4",
    "wmv",
    "mpg",
]


def is_meta_file(filename):
    return filename.startswith("._")


def compress_file(file_, delete):
    in_filename = str(file_)
    if in_filename.endswith(OUTPUT_SUFFIX):
        return
    elif is_meta_file(file_.name):
        return
    try:
        call_ffmpeg(in_filename)
    except Exception:
        return
    if delete:
        os.remove(in_filename)


def call_ffmpeg(in_filename):
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


@click.command()
@click.option("--delete", default=False, is_flag=True)
@click.argument("initial_path")
def cli(initial_path, delete):
    p = Path(initial_path)
    if p.is_dir():
        for extension in EXTENSION_LIST:
            for file_ in p.glob("**/*.{}".format(extension)):
                compress_file(file_, delete)
    else:
        compress_file(p, delete)


if __name__ == "__main__":
    cli()
