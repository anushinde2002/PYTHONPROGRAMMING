import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, f"{celsius:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Celsius to Fahrenheit
label_celsius = ttk.Label(root, text="Celsius:")
label_celsius.grid(column=0, row=0, padx=10, pady=10)

entry_celsius = ttk.Entry(root)
entry_celsius.grid(column=1, row=0, padx=10, pady=10)

button_celsius_to_fahrenheit = ttk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
button_celsius_to_fahrenheit.grid(column=2, row=0, padx=10, pady=10)

# Fahrenheit to Celsius
label_fahrenheit = ttk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(column=0, row=1, padx=10, pady=10)

entry_fahrenheit = ttk.Entry(root)
entry_fahrenheit.grid(column=1, row=1, padx=10, pady=10)

button_fahrenheit_to_celsius = ttk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius)
button_fahrenheit_to_celsius.grid(column=2, row=1, padx=10, pady=10)

root.mainloop()
