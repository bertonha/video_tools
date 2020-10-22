import click

from video_tools.commands import sources

cli = click.CommandCollection(sources=sources)

if __name__ == "__main__":
    cli()
