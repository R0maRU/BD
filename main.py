import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == "0":
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in "+-/*":
        value = value[:-1]
    elif "+" in value or "-" in value or "/" in value or "*" in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Warning!", "You can't use letter, numbers only.")
        calc.insert(0, 0)
    except (ZeroDivisionError):
        messagebox.showinfo("Warning!", "You can't divide by zero")
        calc.insert(0, 0)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def make_digit_button(digit):
    return tk.Button(text=digit, font=("Arial", 15, "bold"), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, font=("Arial", 25), fg="green", command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, font=("Arial", 25), bg="green", command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, font=("Arial", 25), fg="orange", command=clear)


win = tk.Tk()
win.title("Calculator")
icon = tk.PhotoImage(file="calculator1.png")
win.iconphoto(True, icon)
win.geometry(f"245x300")

calc = tk.Entry(win, justify=tk.RIGHT, bd=2, font=("Arial", 20))
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="wens")

make_digit_button("9").grid(row=1, column=2, stick="wens")
make_digit_button("8").grid(row=1, column=1, stick="wens")
make_digit_button("7").grid(row=1, column=0, stick="wens")
make_digit_button("6").grid(row=2, column=2, stick="wens")
make_digit_button("5").grid(row=2, column=1, stick="wens")
make_digit_button("4").grid(row=2, column=0, stick="wens")
make_digit_button("3").grid(row=3, column=2, stick="wens")
make_digit_button("2").grid(row=3, column=1, stick="wens")
make_digit_button("1").grid(row=3, column=0, stick="wens")
make_digit_button("0").grid(row=4, column=1, stick="wens")

make_operation_button("+").grid(row=1, column=3, sticky="wens")
make_operation_button("-").grid(row=2, column=3, sticky="wens")
make_operation_button("/").grid(row=3, column=3, sticky="wens")
make_operation_button("*").grid(row=4, column=3, sticky="wens")

make_calc_button("=").grid(row=4, column=2, sticky="wens")

make_clear_button("C").grid(row=4, column=0, sticky="wens")

win.grid_columnconfigure(0, weight=1, minsize=60)
win.grid_columnconfigure(1, weight=1, minsize=60)
win.grid_columnconfigure(2, weight=1, minsize=60)
win.grid_columnconfigure(3, weight=1, minsize=60)

win.grid_rowconfigure(0, weight=1, minsize=60)
win.grid_rowconfigure(1, weight=1, minsize=60)
win.grid_rowconfigure(2, weight=1, minsize=60)
win.grid_rowconfigure(3, weight=1, minsize=60)
win.grid_rowconfigure(4, weight=1, minsize=60)

win.mainloop()
