import pathlib
import sys

import typer


def main(require: str = typer.Option('', case_sensitive=False),
         exclude: str = typer.Option('', case_sensitive=False),
         nail: str = typer.Option('.....', case_sensitive=False),
         deny: tuple[str, str, str, str, str] = typer.Option(tuple('.....'), case_sensitive=False)) -> None:

    with open(pathlib.Path(sys.argv[0]).cwd() / 'wordles.txt', encoding='utf-8') as fp:
        wordles = set(fp.read().strip().split())

    excluded = set(exclude.lower())
    required = set(require.lower()) - excluded
    nailed = (nail + '.....')[:5].lower()

    nailed = [('.' if ch in excluded else ch) for ch in nailed]
    required.update({ch for ch in nailed if ch != '.'})
    denied = [(s.lower() if nailed[i] == '.' else '.') for i, s in enumerate(deny)]

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

    print(sorted(wordles))


if __name__ == '__main__':
    typer.run(main)
