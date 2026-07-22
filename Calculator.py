import tkinter as tk


def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("320x420")
window.resizable(False, False)

entry = tk.Entry(
    window,
    font=("Arial", 20),
    justify="right",
    bd=10
)
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            command = calculate
        elif btn == "C":
            command = clear
        else:
            command = lambda x=btn: click(x)

        tk.Button(
            frame,
            text=btn,
            font=("Arial", 18),
            command=command
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)

window.mainloop()
