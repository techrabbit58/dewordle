# dewordle
Help for solving (german) wordle puzzles.

## extract_fiveletter_words.py
Use this to download a list of german words and then extract only fiveletter words.
Does require the external library "[requests]".
Try the "--help" function of the program.

## count_letter_frequencies.py
Use this to analyze the fiveletter words list and to
find the five most common letters in each letter
position.

## dewordle.py
Use this to help you when you tray to solve (german)
wordles.
Does require the external libraries "[typer]" and "[rich]".
Try the "--help" function of the program.

[requests]: https://pypi.org/project/requests/
[typer]: https://pypi.org/project/typer/
[rich]: https://pypi.org/project/rich/
