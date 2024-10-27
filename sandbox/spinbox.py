import tkinter as tk
from tkinter import ttk


def main() -> None:
    # root window
    root = tk.Tk()
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('Spinbox Demo')

    label = ttk.Label(root, text='Choose a Number')
    label.pack(pady=5)

    # Spinbox
    current_value = tk.IntVar(value=0)
    spin_box = ttk.Spinbox(
        root,
        from_=0,
        to=30,
        textvariable=current_value,
        wrap=True)

    spin_box.pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
