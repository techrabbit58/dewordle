import argparse
from collections import Counter


def parse_args(prog: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=prog,
        description='Count letter frequencies of first five letters of words.'
    )
    parser.add_argument(
        'wordlist',
        type=argparse.FileType('r', encoding='utf8'),
        help='the text file containing the words'
    )
    return parser.parse_args()


def main(prog: str):
    args = parse_args(prog)
    counters = [Counter() for _ in range(5)]
    for word in args.wordlist.read().split():
        for i, letter in enumerate(word.lower()):
            if i < 5:
                counters[i][letter] += 1
    for i, counter in enumerate(counters):
        print(f'{i}: {counter.most_common(5)}')


if __name__ == '__main__':
    main(prog='count_letter_frequencies')
