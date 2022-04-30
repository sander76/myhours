from importlib import metadata
from pathlib import Path

import typer

from myhours.console import info, warn
from myhours.extract import process_folder

app = typer.Typer()


@app.command()
def version():
    """Print the app version"""
    info(f"Myhours version: {metadata.version(__package__)}")


@app.command()
def manage(
    input_folder: Path = typer.Argument(
        Path.cwd(), help="Path with excel files.", dir_okay=True
    )
) -> None:
    info(f"Parsing excel files in {input_folder}")
    output_folder = input_folder / "output"
    if not output_folder.exists():
        warn(f"Output folder does not exist. {output_folder}")
        raise typer.Exit()

    process_folder(input_folder, output_folder)


def run():
    app()
