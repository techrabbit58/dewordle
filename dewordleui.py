import pathlib
import sys
import tkinter as tk
from functools import partial

SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
DEFAULT, GREY, YELLOW, GREEN = 'white grey yellow lime'.split()
COLORS = [DEFAULT, GREY, YELLOW, GREEN]
DEFAULT_BG = 'lightblue'


def main(prog: str) -> None:
    root = tk.Tk()

    root.title(prog)
    root.configure(bg=DEFAULT_BG)

    symbol_btns = []
    symbol_colors = [0] * len(SYMBOLS)
    groups = {
        'white': set(SYMBOLS),
        'grey': set(),
        'yellow': set(),
        'lime': set(),
    }

    def on_click(btn: int) -> None:
        symbol = symbol_btns[btn].cget('text')
        color = symbol_colors[btn]
        groups[COLORS[color]].remove(symbol)
        color = (color + 1) % len(COLORS)
        symbol_btns[btn].configure(bg=COLORS[color])
        symbol_colors[btn] = color
        groups[COLORS[color]].add(symbol)

    def on_select() -> None:
        print('SELECTION')

    btn_args = dict(font='Arial 16 bold', width=2)

    line1 = tk.Frame(root, padx=10, pady=10, bg=DEFAULT_BG)
    line1.pack()

    for i in range(9):
        n = i
        symbol_btns.append(tk.Button(line1, text=SYMBOLS[n], command=partial(on_click, n), **btn_args))
        symbol_btns[-1].configure(bg=COLORS[symbol_colors[n]])
        symbol_btns[-1].grid(row=0, column=i)

    line2 = tk.Frame(root, padx=10, bg=DEFAULT_BG)
    line2.pack()

    for i in range(8):
        n = 9 + i
        symbol_btns.append(tk.Button(line2, text=SYMBOLS[n], command=partial(on_click, n), **btn_args))
        symbol_btns[-1].configure(bg=COLORS[symbol_colors[n]])
        symbol_btns[-1].grid(row=0, column=i)

    line3 = tk.Frame(root, padx=10, pady=10, bg=DEFAULT_BG)
    line3.pack()

    for i in range(9):
        n = 17 + i
        symbol_btns.append(tk.Button(line3, text=SYMBOLS[n], command=partial(on_click, n), **btn_args))
        symbol_btns[-1].configure(bg=COLORS[symbol_colors[n]])
        symbol_btns[-1].grid(row=0, column=i)

    buttons = tk.Frame(root)
    buttons.pack()

    tk.Button(buttons, text='Select', padx=20, pady=10, command=on_select, font='bold').grid(row=0, column=0)
    tk.Button(buttons, text='Quit', padx=20, pady=10, command=root.destroy, font='bold').grid(row=0, column=1)
    tk.Label(root, bg='lightblue').pack()

    root.mainloop()


if __name__ == '__main__':
    main('De-Wordle')
