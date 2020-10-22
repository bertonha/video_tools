from pathlib import Path

import click

from video_tools.utils import delete_file, is_meta_file


@click.group()
def cleanup_group():
    pass


@cleanup_group.command()
@click.argument("initial_path", type=click.Path(exists=True))
def cleanup(initial_path):
    p = Path(initial_path)
    for file_ in p.glob("**/*"):
        if is_meta_file(file_):
            delete_file(file_)
