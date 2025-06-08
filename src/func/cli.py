import typer
from .utils.init import init_project

__version__ = "0.1.0"

cli = typer.Typer(
    name="func",
    help="My awesome func CLI application!",
    no_args_is_help=True
)

@cli.command()
def init():
    init_project()
    typer.echo("Project initialized successfully!")

@cli.command()
def add(file: str):
    print(f"Running the project: {file}")

@cli.command()
def greet(name: str):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    cli()

