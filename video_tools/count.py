from pathlib import Path

import click

from .utils import print_style


@click.group()
def count_group():
    pass


@count_group.command()
@click.argument("initial_path")
@click.argument("extension")
@click.option("--verbose", default=False, is_flag=True)
def count(initial_path, extension, verbose):
    p = Path(initial_path)
    files = list(p.glob(f"**/*.{extension}"))
    print_style(f"Total {extension} files: {len(files)}")
    if verbose:
        for file_ in files:
            print_style(str(file_), fg="blue")
