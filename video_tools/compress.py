from pathlib import Path

import click

from .utils import (
    call_ffmpeg,
    delete_file,
    filter_compressable_files,
    generate_output_file,
    print_style,
)


@click.group()
def compress_group():
    pass


@compress_group.command()
@click.option("-d", "--delete", default=False, is_flag=True)
@click.argument("initial_path", type=click.Path(exists=True))
def compress(initial_path, delete):
    p = Path(initial_path)

    if p.is_dir():
        files = list(filter_compressable_files(p.glob("**/*.*")))
    else:
        files = [p]

    total_files = len(files)

    for index, in_file in enumerate(files):
        out_file = generate_output_file(in_file)

        print_style(f"Compressing file {index + 1} of {total_files}")
        print_style(f"Input file: {in_file}")
        print_style(f"Output file: {out_file}")

        try:
            call_ffmpeg(in_file, out_file)
        except Exception:
            continue
        if delete and out_file.exists():
            delete_file(in_file)
