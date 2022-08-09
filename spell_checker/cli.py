"""Console script for spell_checker."""
import sys
import click
from spell_checker import spell_checker


@click.command()
def main(args=None):
    spell_checker.check_chinese()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
