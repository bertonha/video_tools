import click

from .cleanup import cleanup_group
from .compress import compress_group
from .count import count_group

sources = [cleanup_group, compress_group, count_group]

cli = click.CommandCollection(sources=sources)

if __name__ == "__main__":
    cli()
