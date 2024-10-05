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

## German Umlaut
You may want to extract german words wit umlaut, for
wordle games that support german umlaut.
Use the extract_fiveletter_words program without
the "-u" option to create a fiveletter file with
umlauted words.

## Engish Wordle
You may want to modify the extract_fiveletter_words
program so that it loads an english word list 
instead of a german word list.
Try this [alternate URL] to get a list of english
words.
The extract_fiveletter_words program does not 
currently provide an option to easily switch between
languages.
The dewordle program does not yet provide a switch
to work with different word lists.

---

[requests]: https://pypi.org/project/requests/
[typer]: https://pypi.org/project/typer/
[rich]: https://pypi.org/project/rich/
[alternate URL]: https://raw.githubusercontent.com/tabatkins/wordle-list/refs/heads/main/words