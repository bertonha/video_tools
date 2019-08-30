from pathlib import Path

import click


@click.group()
def count_group():
    pass


@count_group.command()
@click.argument("initial_path")
@click.argument("extension")
def count(initial_path, extension):
    p = Path(initial_path)
    total = len(list(p.glob(f"**/*.{extension}")))
    click.echo(click.style(f"Total {extension} files: {total}"))
