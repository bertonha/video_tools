import os
import subprocess

import click
from pathlib import Path


OUTPUT_SUFFIX = "_compressed.mp4"


def is_meta_file(filename):
    return filename.startswith("._")


def compress_file(file_, delete):
    in_filename = str(file_)
    if in_filename.endswith(OUTPUT_SUFFIX):
        return
    elif is_meta_file(file_.name):
        return
    call_ffmpeg(in_filename)
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
@click.option("--input_ext", default="MP4")
@click.argument("initial_path")
def cli(initial_path, delete, input_ext):
    p = Path(initial_path)
    if p.is_dir():
        for file_ in p.glob("**/*.{}".format(input_ext)):
            compress_file(file_, delete)
    else:
        compress_file(p, delete)


if __name__ == "__main__":
    cli()
