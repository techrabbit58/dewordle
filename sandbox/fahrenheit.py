import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


class TemperatureConverter(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)

        style_settings = { 'font': ('Helvetica', 11)}

        self.style = ttk.Style(master)
        self.style.configure('TLabel', **style_settings)
        self.style.configure('TButton', **style_settings)

        field_padding = {'padx': 5, 'pady': 5}

        self.fahrenheit = tk.StringVar()

        self.temperature_label = ttk.Label(self, text='Fahrenheit')
        self.temperature_label.grid(column=0, row=0, sticky=tk.W, **field_padding)

        self.temperature_entry = ttk.Entry(self, textvariable=self.fahrenheit)
        self.temperature_entry.grid(column=1, row=0, sticky=tk.W, **field_padding)
        self.temperature_entry.bind('<Return>', lambda _: self.convert())
        self.temperature_entry.focus()

        self.converter_button = ttk.Button(self, text='Convert', command=self.convert)
        self.converter_button.grid(column=2, row=0, sticky=tk.W, **field_padding)

        self.celsius_label = ttk.Label(self)
        self.celsius_label.grid(columnspan=3, row=1, **field_padding)

        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def convert(self) -> None:
        try:
            f = float(self.fahrenheit.get())
            c = fahrenheit_to_celsius(f)
            self.celsius_label['text'] = f'{f:.1f} °F = {c:.1f} °C'
        except ValueError as error:
            showerror(title='Value Error', message=str(error))


class App(tk.Tk):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.title(title)
        self.resizable(width=False, height=False)


if __name__ == '__main__':
    app = App('Temperature Converter')
    TemperatureConverter(app)
    app.mainloop()
