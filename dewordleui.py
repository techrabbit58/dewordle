import contextlib
import functools
import textwrap
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
WORDLES_FILE = 'wordles.txt'


@contextlib.contextmanager
def widget_as_normal(widget):
    original_state, widget['state'] = widget['state'], tk.NORMAL
    yield widget
    widget['state'] = original_state


class App(tk.Tk):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.wordles: list[str] = []

        self.resizable(width=False, height=False)
        self.title(title)

        common_conf = dict(padx=5, pady=5, anchor=tk.W)

        grey_validator = (self.register(self.validate_grey), '%P')
        yellow_validator = (self.register(self.validate_yellow), '%P')
        is_not_valid = (self.register(self.entry_not_valid),)

        l_grey = ttk.Label(self, text='Grey Letters')
        l_grey.pack(**common_conf)

        self.grey_letters = tk.StringVar()
        e_grey = ttk.Entry(
            self,
            textvariable=self.grey_letters,
            width=30,
            font=('Courier', 11),
            validate='key',
            validatecommand=grey_validator,
            invalidcommand=is_not_valid)
        e_grey.pack(fill=tk.X, ipady=3, **common_conf)

        l_yellow = ttk.Label(self, text='Yellow Letters')
        l_yellow.pack(**common_conf)

        f_yellow = ttk.Frame(self)
        f_yellow.pack(expand=True, fill=tk.X)

        yellow_entries = []
        self.yellow_letters = []
        for i in range(5):
            self.yellow_letters.append(tk.StringVar())
            yellow_entries.append(
                ttk.Entry(
                    f_yellow,
                    width=9,
                    textvariable=self.yellow_letters[i],
                    font=('Courier', 11),
                    validate='key',
                    validatecommand=yellow_validator,
                    invalidcommand=is_not_valid))
            yellow_entries[i].pack(side=tk.LEFT, fill=tk.X, ipady=3, expand=True, **common_conf)

        l_green = ttk.Label(self, text='Green Letters')
        l_green.pack(**common_conf)

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
                    width=10,
                    state='readonly',
                    textvariable=self.green_letters[i],
                    font=('Courier', 11)))
            green_entries[i].pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=3, **common_conf)
            green_entries[i].bind(
                '<<ComboboxSelected>>',
                functools.partial(self.validate_green, green_entries[i]))

        l_words = ttk.Label(self, text='Proposed Wordle Words')
        l_words.pack(side=tk.TOP, **common_conf)

        self.t_words = scrolledtext.ScrolledText(
            self, height=10, width=60, wrap=tk.WORD, font=('Courier', 11), spacing2=4, spacing3=4)
        self.t_words.pack(fill=tk.X, **common_conf)
        self.t_words['state'] = tk.DISABLED

        b_select = ttk.Button(self, text='Select', command=self.perform_selection)
        b_select.pack(side=tk.LEFT, **common_conf)

        b_reset = ttk.Button(self, text='Reset', command=self.reset_dewordle)
        b_reset.pack(side=tk.LEFT, **common_conf)

        b_quit = ttk.Button(self, text='Quit', command=self.destroy)
        b_quit.pack(side=tk.LEFT, **common_conf)

        rootstyle = ttk.Style(self)
        rootstyle.configure('TLabel', font=('TkDefaultFont', 11))
        rootstyle.configure('TButton', font=('TkDefaultFont', 11))

        self.default_widget = e_grey

        self.bind('<Return>', self.perform_selection)

        self.reset_dewordle()

    def perform_selection(self, _ = None) -> None:
        grey_letters = set(self.grey_letters.get())
        yellow_letters = [set(letters.get()) for letters in self.yellow_letters]
        green_letters = [letter.get() for letter in self.green_letters]
        with widget_as_normal(self.t_words) as widget:
            widget.delete('1.0', tk.END)
            for word in self.wordles:
                if grey_letters.intersection(word):
                    continue
                reject = False
                for i, letter in enumerate(word):
                    if letter in yellow_letters[i]:
                        reject = True
                        break
                if reject:
                    continue
                for i, letter in enumerate(green_letters):
                    if letter == '.':
                        continue
                    if letter != word[i]:
                        reject = True
                        break
                if not reject:
                    widget.insert(tk.END, word.ljust(6, ' '))

    def reset_dewordle(self) -> None:
        self.grey_letters.set('')

        for widget in self.yellow_letters:
            widget.set('')

        for widget in self.green_letters:
            widget.set('.')

        with widget_as_normal(self.t_words) as widget:
            widget.delete('1.0', tk.END)

        self.default_widget.focus()

        with open(WORDLES_FILE, encoding='utf-8') as wf:
            self.wordles = wf.read().strip().lower().split()

    @staticmethod
    def validate_symbols(value: str) -> bool:
        chars = set(value)
        if len(chars) != len(value):
            return False
        for c in value:
            if c not in SYMBOLS:
                return False
        return True

    def validate_grey(self, value: str) -> bool:
        if self.validate_symbols(value):
            for var in self.yellow_letters:
                var.set(''.join(symbol for symbol in var.get() if symbol not in value))
            for var in self.green_letters:
                symbol = var.get()
                var.set('.' if symbol in value else symbol)
            return True
        else:
            return False

    def validate_yellow(self, value: str) -> bool:
        if self.validate_symbols(value):
            grey_letters = self.grey_letters.get()
            for letter in value:
                if letter in grey_letters:
                    return False
            return True
        else:
            return False

    def validate_green(self, widget: ttk.Combobox, _) -> None:
        value = self.getvar(widget['textvariable'])
        if value in self.grey_letters.get():
            self.entry_not_valid()
            self.setvar(widget['textvariable'], '.')

    @staticmethod
    def entry_not_valid() -> None:
        messagebox.showinfo('Bad Entry', message=textwrap.dedent(f"""
        You may only enter valid symbols out of the set "{SYMBOLS}".
        Every symbol may only appear once.
        Grey letters cannot be used as yellow or green choices at the same time.
        """))


if __name__ == '__main__':
    App('De-Wordle Assistant').mainloop()
