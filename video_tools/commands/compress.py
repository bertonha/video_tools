from pathlib import Path

import click

from video_tools.utils import (
    call_ffmpeg,
    delete_file,
    filter_compressible_files,
    generate_output_filename,
    print_style,
)


@click.group()
def compress_group():
    pass


@compress_group.command()
@click.option("-r", "--rotate", default=False, is_flag=True)
@click.option("-d", "--delete", default=False, is_flag=True)
@click.option("--resolution", default=None)
@click.argument("initial_path", type=click.Path(exists=True))
def compress(initial_path, delete, rotate, resolution):
    p = Path(initial_path)

    if p.is_dir():
        files = list(filter_compressible_files(p.glob("**/*.*")))
    else:
        files = [p]

    total_files = len(files)

    for index, in_file in enumerate(files):
        out_file = generate_output_filename(in_file)

        print_style(f"Compressing file {index + 1} of {total_files}")
        print_style(f"Input file: {in_file}")
        print_style(f"Output file: {out_file}")

        try:
            call_ffmpeg(in_file, out_file, rotate, resolution)
        except Exception:
            continue
        else:
            if delete and out_file.exists():
                delete_file(in_file)
