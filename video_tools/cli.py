import click

from video_tools.commands.cleanup import cleanup_group
from video_tools.commands.compress import compress_group
from video_tools.commands.count import count_group

sources = [cleanup_group, compress_group, count_group]

cli = click.CommandCollection(sources=sources)

if __name__ == "__main__":
    cli()
