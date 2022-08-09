"""Console script for spell_checker."""
import os
import sys
import click
from spell_checker import spell_checker


@click.command()
@click.option('--check', help='Type of check to do.')
def main(check):
    pass


def check_chinese():
    cwd = os.getcwd()
    changed_filenames = sys.argv[1:]
    print(changed_filenames)

    should_fail = False
    for filename in changed_filenames:
        file_path = os.path.join(cwd, filename)
        chinese_exists, all_chinese = spell_checker.check_chinese(file_path)
        print("Found file containing Chinese: %s" % filename)
        print("".join(all_chinese))
        if chinese_exists:
            should_fail = True

    if should_fail:
        exit(1)


if __name__ == "__main__":
    sys.exit(main())
