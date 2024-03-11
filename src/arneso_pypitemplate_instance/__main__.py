"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Arneso Pypitemplate Instance."""


if __name__ == "__main__":
    main(prog_name="arneso-pypitemplate-instance")  # pragma: no cover
