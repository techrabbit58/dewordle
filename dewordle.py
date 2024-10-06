import pathlib
import sys

import typer
from rich import print, get_console


def main(
        exclude: str = typer.Option(
            '', case_sensitive=False,
            help='exclude words contining these letters'),
        nail: str = typer.Option(
            '.....', case_sensitive=False,
            help='letters that are required exactly at that position'),
        deny: tuple[str, str, str, str, str] = typer.Option(
            tuple('.....'), case_sensitive=False,
            help='do not include words with these letters in that positions')) -> None:
    """Help solving a german "wordle" puzzle by filtering a list of fiveletter words."""

    with open(pathlib.Path(sys.argv[0]).cwd() / 'wordles.txt', encoding='utf-8') as fp:
        wordles = set(fp.read().strip().split())

    excluded = set(exclude.lower())
    nailed = (nail + '.....')[:5].lower()

    nailed = [('.' if ch in excluded else ch) for ch in nailed]
    required = {ch for ch in nailed if ch != '.'}

    denied = [(s.lower() if nailed[i] == '.' else '.') for i, s in enumerate(deny)]
    required.update(set(''.join(ch for ch in denied if ch != '.')))

    print(f'{excluded=}')
    print(f'{required=}')
    print(f'{nailed=}')
    print(f'{denied=}')

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

    candidates = set()
    for word in wordles:
        for i in range(len(nailed)):
            if nailed[i] != '.' and word[i] != nailed[i]:
                break
        else:
            candidates.add(word)
    wordles = candidates

    candidates = set()
    for word in wordles:
        for i, d in enumerate(denied):
            if word[i] in d:
                break
        else:
            candidates.add(word)
    wordles = candidates

    console = get_console()
    width = console.width + 1

    line = []
    for word in sorted(wordles):
        if (len(line) + 1) * 6 < width:
            line.append(word)
        else:
            console.print(' '.join(line), style='cyan')
            line = []
    console.print(' '.join(line), style='cyan')


if __name__ == '__main__':
    typer.run(main)
