import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.resizable(width=False, height=False)
        self.title(title)

        properties = dict(padx=5, pady=5, anchor=tk.W)

        l_grey = ttk.Label(self, text='Grey Letters')
        l_grey.pack(**properties)

        e_grey = ttk.Entry(self)
        e_grey.pack(fill=tk.X, **properties)

        l_yellow = ttk.Label(self, text='Yellow Letters')
        l_yellow.pack(**properties)

        f_yellow = ttk.Frame(self)
        f_yellow.pack(**properties)

        yellow_entries = []
        for i in range(5):
            yellow_entries.append(ttk.Entry(f_yellow))
            yellow_entries[i].pack(side=tk.LEFT, **properties)

        l_green = ttk.Label(self, text='Green Letters')
        l_green.pack(**properties)

        f_green = ttk.Frame(self)
        f_green.pack(**properties)

        green_entries = []
        for i in range(5):
            green_entries.append(ttk.Entry(f_green))
            green_entries[i].pack(side=tk.LEFT, **properties)

        l_words = ttk.Label(self, text='Proposed Wordle Words')
        l_words.pack(side=tk.TOP, **properties)

        t_words = tk.Text(self, height=10)
        t_words.pack(fill=tk.X, **properties)

        b_quit = ttk.Button(self, text='Quit', command=lambda: self.destroy())
        b_quit.pack(**properties)

        style = ttk.Style(self)
        style.configure('TLabel', font=('Helvetica', 11))
        style.configure('TEntry', font=('Helvetica', 11))
        style.configure('TButton', font=('Helvetica', 11))


if __name__ == '__main__':
    App('De-Wordle Assistant').mainloop()
