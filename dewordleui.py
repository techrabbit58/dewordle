import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.geometry('300x80')
        self.resizable(width=False, height=False)
        self.title(title)

        padding = dict(padx=5, pady=5)

        l_hello = ttk.Label(self, text='Hello, world!')
        l_hello.pack(**padding)

        b_quit = ttk.Button(self, text='Quit', command=lambda: self.destroy())
        b_quit.pack(**padding)

        style = ttk.Style(self)
        style.configure('TLabel', font=('Helvetica', 11))
        style.configure('T^Button', font=('Helvetica', 11))


if __name__ == '__main__':
    App('De-Wordle assistant').mainloop()
