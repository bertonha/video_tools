from pathlib import Path

import click

from .utils import print_style


@click.group()
def count_group():
    pass


@count_group.command()
@click.argument("initial_path")
@click.argument("extension")
def count(initial_path, extension):
    p = Path(initial_path)
    total = len(list(p.glob(f"**/*.{extension}")))
    print_style(f"Total {extension} files: {total}")
