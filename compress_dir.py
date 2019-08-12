import os
import subprocess

import click
from pathlib import Path


OUTPUT_SUFFIX = "_compressed.mp4"


def compress_file(in_filename):
    out_filename = "{}{}".format(in_filename[:-4], OUTPUT_SUFFIX)
    subprocess.run(
        [
            "ffmpeg",
            "-i", str(in_filename),
            "-c:v", "libx265",
            "-crf", "28",
            "-c:a", "aac", "-b:a", "128k",
            out_filename,
        ],
        check=True,
    )


@click.command()
@click.option("--delete", default=False, is_flag=True)
@click.option("--input_ext", default="mp4")
@click.argument("initial_path")
def cli(initial_path, delete, input_ext):
    p = Path(initial_path)
    for in_filename in p.glob("**/*.{}".format(input_ext)):
        if str(in_filename).endswith(OUTPUT_SUFFIX):
            continue
        compress_file(str(in_filename))
        if delete:
            os.remove(str(in_filename))


if __name__ == "__main__":
    cli()
