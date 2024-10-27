import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        root = self

        root.geometry('300x150')
        root.resizable(width=False, height=False)
        root.title('Login')

        # UI options
        padding = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)

        # create variables
        username = tk.StringVar()
        password = tk.StringVar()

        # heading
        heading = ttk.Label(root, text='Member Login', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        # create labels and entries: username
        l_username = ttk.Label(root, text='Username')
        l_username.grid(row=1, column=0, sticky=tk.W, **padding)

        e_username = ttk.Entry(root, textvariable=username, **entry_font)
        e_username.grid(column=1, row=1, sticky=tk.E, **padding)

        # create labels and entries: password
        l_password = ttk.Label(root, text='Password')
        l_password.grid(row=2, column=0, sticky=tk.W, **padding)

        # hidden password symbols due to the 'show' property
        e_password = ttk.Entry(root, textvariable=password, show="*", **entry_font)
        e_password.grid(column=1, row=2, sticky=tk.E, **padding)

        # the 'Login' button
        b_login = ttk.Button(root, text="Login")
        b_login.grid(column=1, row=3, sticky=tk.E, **padding)

        # configure style
        self.style = ttk.Style(root)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))


if __name__ == '__main__':
    App().mainloop()
