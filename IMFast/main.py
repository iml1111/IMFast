"""
Application Management Module
"""
import click
from fastapi import FastAPI
from app import create_app
from settings import settings

application: FastAPI = create_app(settings)


@click.group()
def cli():
    """Command Groups"""


@cli.command()
def run():
    """Please use 'imfast run'."""
    raise NotImplementedError("Please use 'imfast.sh run'.")


@cli.command()
def prod_run():
    """Please use 'imfast prod-run'."""
    raise NotImplementedError("Please use 'imfast.sh prod-run'.")


@cli.command()
def init_db():
    """Sample command"""
    click.echo('Initialized the database (if necessary)')


@cli.command()
def routes():
    """Print all routes"""
    click.echo('# Routes')
    routes = []
    path_len = 0
    method_len = 0
    name_len = 0

    for route in application.routes:
        routes.append((
            route.path, str(route.methods), route.name))
        path_len = max(path_len, len(route.path))
        method_len = max(method_len, len(str(route.methods)))
        name_len = max(name_len, len(route.name))

    click.echo(
        f"{'Path ':=<{path_len + 2}}"
        f"{' Methods ':=<{method_len + 1}}"
        f"{' Name ':=<{name_len + 1}}")
    for route in sorted(routes):
        click.echo(
            f'{route[0]: <{path_len + 2}}'
            f'{route[1]: <{method_len + 2}}'
            f'{route[2]: <{name_len + 2}}')


@cli.command()
def test():
    """Run tests"""
    raise NotImplementedError("Please use 'imfast test'.")

if __name__ == '__main__':
    cli()
