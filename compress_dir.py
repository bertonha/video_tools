import os
import subprocess

import click
from pathlib import Path


@click.command()
@click.option("--delete", default=False, is_flag=True)
@click.argument("initial_path")
def main(initial_path, delete):
    p = Path(initial_path)
    for in_filename in p.glob("**/*.mp4"):
        out_filename = "{}_compressed.mp4".format(str(in_filename)[:-4])
        subprocess.run([
            "ffmpeg",
            "-i", str(in_filename),
            "-c:v", "libx265",
            "-crf", "28",
            "-c:a", "aac", "-b:a", "128k",
            out_filename,
        ], check=True)
        if delete:
            os.remove(str(in_filename))


if __name__ == "__main__":
    main()
