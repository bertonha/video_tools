from collections import Counter
from pathlib import Path

import click

from video_tools.utils import print_style


@click.group()
def count_group():
    pass


@count_group.command()
@click.option("-v", "--verbose", default=False, is_flag=True)
@click.argument("initial_path", type=click.Path(exists=True))
@click.argument("extensions", required=False, nargs=-1)
def count(initial_path, extensions, verbose):
    p = Path(initial_path)
    counter = Counter()
    for file_ in p.glob("**/*.*"):
        counter[file_.suffix.lower()] += 1

    if not extensions:
        extensions = list(counter.keys())

    for extension in extensions:
        print_style(f"Total {extension} files: {counter[extension.lower()]}")
        if verbose:
            for file_ in p.glob(f"**/*{extension}"):
                print_style(str(file_), fg="blue")
