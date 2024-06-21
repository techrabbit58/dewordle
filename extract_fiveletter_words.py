import argparse
import textwrap

import requests

wordlist_url = 'https://raw.githubusercontent.com/davidak/wortliste/master/wortliste.txt'

prog_description = textwrap.dedent(f"""
Extract all five letter words from the input at {wordlist_url}.
Create an output file with the extracted words, one line per word,
with all words normalized to lowercase.
""").strip()


def expand_umlaut(word: str) -> str:
    letters = []
    for letter in list(word):
        match letter:
            case 'ä':
                letters.append('ae')
            case 'ö':
                letters.append('oe')
            case 'ü':
                letters.append('ue')
            case 'ß':
                letters.append('ss')
            case _:
                letters.append(letter)
    return ''.join(letters)


def main(prog: str) -> None:
    args = parse_args(prog)
    history = set()
    infile = requests.get(wordlist_url).text.split()
    for word in infile:
        word = word.lower()
        if args.no_umlaut:
            word = expand_umlaut(word)
        if len(word) == 5 and word not in history:
            print(word, file=args.outfile)
            history.add(word)


def parse_args(prog: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=prog,
        description=prog_description
    )
    parser.add_argument(
        'outfile',
        type=argparse.FileType('x', encoding='utf8'),
        help='this file gets opened for writing, but only if it does not exist'
    )
    parser.add_argument(
        '-u', '--no_umlaut',
        help='make a word list that does not contain words with umlaut',
        action='store_true'
    )
    return parser.parse_args()


if __name__ == '__main__':
    main('extract_five_letter_words')
