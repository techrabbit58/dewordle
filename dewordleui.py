import tkinter as tk
from tkinter import ttk, font, scrolledtext


class App(tk.Tk):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.resizable(width=False, height=False)
        self.title(title)

        appearance = dict(padx=5, pady=5, anchor=tk.W)

        l_grey = ttk.Label(self, text='Grey Letters')
        l_grey.pack(**appearance)

        e_grey = ttk.Entry(self)
        e_grey.pack(fill=tk.X, **appearance)

        l_yellow = ttk.Label(self, text='Yellow Letters')
        l_yellow.pack(**appearance)

        f_yellow = ttk.Frame(self)
        f_yellow.pack(expand=True, fill=tk.X)

        yellow_entries = []
        for i in range(5):
            yellow_entries.append(ttk.Entry(f_yellow, width=10))
            yellow_entries[i].pack(side=tk.LEFT, fill=tk.X, expand=True, **appearance)

        l_green = ttk.Label(self, text='Green Letters')
        l_green.pack(**appearance)

        f_green = ttk.Frame(self)
        f_green.pack()

        green_entries = []
        for i in range(5):
            green_entries.append(ttk.Combobox(f_green, width=13))
            green_entries[i].pack(side=tk.LEFT, fill=tk.X, expand=True, **appearance)

        l_words = ttk.Label(self, text='Proposed Wordle Words')
        l_words.pack(side=tk.TOP, **appearance)

        t_words = scrolledtext.ScrolledText(
            self, height=10, width=60, wrap=tk.WORD, font=('TkFixedFont', 11), spacing2=3)
        t_words.pack(fill=tk.X, **appearance)
        for word in font.names():
            t_words.insert(tk.END, word.ljust(20, ' '))
        t_words['state'] = tk.DISABLED

        b_quit = ttk.Button(self, text='Quit', command=lambda: self.destroy())
        b_quit.pack(**appearance)

        style = ttk.Style(self)
        style.configure('TLabel', font=('TkDefaultFont', 11))
        style.configure('TEntry', font=('TkFixedFont', 11))
        style.configure('TButton', font=('TkDefaultFont', 11))
        style.configure('TCombobox', font=('TkFixedFont', 11))

        b_quit.focus()


if __name__ == '__main__':
    App('De-Wordle Assistant').mainloop()
