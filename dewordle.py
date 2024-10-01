import pathlib
import string
import sys

import typer


def main(require: str = typer.Option(string.ascii_lowercase, case_sensitive=False),
         exclude: str = typer.Option('', case_sensitive=False),) -> None:

    with open(pathlib.Path(sys.argv[0]).cwd() / 'wordles.txt', encoding='utf-8') as fp:
        wordles = set(fp.read().strip().split())

    required = set(require.lower())
    excluded = set(exclude.lower()) - required

    print(f'{excluded=}')
    print(f'{required=}')

    candidates = set()
    for word in wordles:
        if excluded.intersection(word):
            candidates.add(word)
    wordles = wordles - candidates

    candidates = set()
    for word in wordles:
        chars = set(word)
        if chars.issuperset(required):
            candidates.add(word)
    wordles = candidates

    print(wordles)


if __name__ == '__main__':
    typer.run(main)
