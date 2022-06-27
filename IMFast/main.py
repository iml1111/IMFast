"""
Application Management Module
"""
import click
from app import create_app
from settings import settings

application = create_app(settings)


@click.group()
def cli():
    """Command Groups"""


@cli.command()
def run():
    """Please use 'imfast run'."""
    raise NotImplementedError("Please use 'imfast run'.")


@cli.command()
def prod_run():
    """Please use 'imfast prod-run'."""
    raise NotImplementedError("Please use 'imfast prod-run'.")


@cli.command()
def init_db():
    """Sample command"""
    click.echo('Initialized the database')


if __name__ == '__main__':
    cli()
