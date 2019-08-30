import click

from .cleanup import cleanup_group
from .compress import compress_group


cli = click.CommandCollection(sources=[cleanup_group, compress_group])
cli()
