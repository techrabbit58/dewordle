import random
import tkinter as tk
from tkinter import ttk, scrolledtext

SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'


class App(tk.Tk):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.resizable(width=False, height=False)
        self.title(title)

        appearance = dict(padx=5, pady=5, anchor=tk.W)

        l_grey = ttk.Label(self, text='Grey Letters')
        l_grey.pack(**appearance)

        self.grey_letters = tk.StringVar()
        e_grey = ttk.Entry(self, textvariable=self.grey_letters, width=30, font=('Courier', 11))
        e_grey.pack(fill=tk.X, **appearance)

        l_yellow = ttk.Label(self, text='Yellow Letters')
        l_yellow.pack(**appearance)

        f_yellow = ttk.Frame(self)
        f_yellow.pack(expand=True, fill=tk.X)

        yellow_entries = []
        self.yellow_letters = []
        for i in range(5):
            self.yellow_letters.append(tk.StringVar())
            yellow_entries.append(
                ttk.Entry(f_yellow, width=9, textvariable=self.yellow_letters[i], font=('Courier', 11)))
            yellow_entries[i].pack(side=tk.LEFT, fill=tk.X, expand=True, **appearance)

        l_green = ttk.Label(self, text='Green Letters')
        l_green.pack(**appearance)

        f_green = ttk.Frame(self)
        f_green.pack()

        green_entries = []
        self.green_letters = []
        for i in range(5):
            self.green_letters.append(tk.StringVar())
            green_entries.append(
                ttk.Combobox(
                    f_green,
                    values=tuple('.' + SYMBOLS),
                    width=9,
                    state='readonly',
                    textvariable=self.green_letters[i],
                    font=('Courier', 11)))
            green_entries[i].pack(side=tk.LEFT, fill=tk.X, expand=True, **appearance)

        l_words = ttk.Label(self, text='Proposed Wordle Words')
        l_words.pack(side=tk.TOP, **appearance)

        self.t_words = scrolledtext.ScrolledText(
            self, height=10, width=60, wrap=tk.WORD, font=('Courier', 11), spacing2=3)
        self.t_words.pack(fill=tk.X, **appearance)
        self.t_words['state'] = tk.DISABLED

        b_reset = ttk.Button(self, text='Reset', command = self.reset_dewordle)
        b_reset.pack(side=tk.LEFT, **appearance)

        b_quit = ttk.Button(self, text='Quit', command=self.destroy)
        b_quit.pack(**appearance)

        rootstyle = ttk.Style(self)
        rootstyle.configure('TLabel', font=('TkDefaultFont', 11))
        rootstyle.configure('TButton', font=('TkDefaultFont', 11))

        self.reset_dewordle()
        b_quit.focus()

    def reset_dewordle(self) -> None:
        self.grey_letters.set('')

        for widget in self.yellow_letters:
            widget.set('')

        for widget in self.green_letters:
            widget.set('.')

        original_state, self.t_words['state'] = self.t_words['state'], tk.NORMAL

        self.t_words.delete('1.0', tk.END)

        for _ in range(500):
            word = ''.join(random.sample(SYMBOLS, 5))
            self.t_words.insert(tk.END, word.ljust(6, ' '))

        self.t_words['state'] = original_state


if __name__ == '__main__':
    App('De-Wordle Assistant').mainloop()
