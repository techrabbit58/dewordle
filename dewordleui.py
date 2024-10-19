import tkinter as tk
from functools import partial

SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'

def main(prog: str) -> None:
    root = tk.Tk()

    root.title(prog)

    symbol_btns = []
    colors = ['red'] * len(SYMBOLS)

    def on_click(btn: int) -> None:
        color = colors[btn]
        symbol_btns[btn].configure(bg=color)

    btn_args = dict(font='Arial 16 bold', width=2)

    line1 = tk.Frame(root, padx=10, pady=10)
    line1.pack()

    for i in range(9):
        n = i
        symbol_btns.append(tk.Button(line1, text=SYMBOLS[n], command=partial(on_click, n), **btn_args))
        symbol_btns[-1].grid(row=0, column=i)

    line2 = tk.Frame(root, padx=10)
    line2.pack()

    for i in range(8):
        n = 9 + i
        symbol_btns.append(tk.Button(line2, text=SYMBOLS[n], command=partial(on_click, n), **btn_args))
        symbol_btns[-1].grid(row=0, column=i)

    line3 = tk.Frame(root, padx=10, pady=10)
    line3.pack()

    for i in range(9):
        n = 17 + i
        symbol_btns.append(tk.Button(line3, text=SYMBOLS[n], command=partial(on_click, n), **btn_args))
        symbol_btns[-1].grid(row=0, column=i)

    tk.Button(root, text='Quit', padx=20, pady=10, command=root.destroy, font='bold').pack()
    tk.Label(root).pack()

    root.mainloop()


if __name__ == '__main__':
    main('De-Wordle')
