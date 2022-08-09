"""Console script for spell_checker."""
import sys
import click
from spell_checker import spell_checker


@click.command()
@click.option('--check', help='Type of check to do.')
def main(check):
    if not check:
        print("No task specified.")
        exit(1)

    if check.lower() == "chinese":
        spell_checker.check_chinese()
    return 0


def check_chinese(*args, **kargs):
    print(args)
    print(kargs)
    print(sys.argv)
    spell_checker.check_chinese()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
