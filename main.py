import tkinter as tk
from tkinter import messagebox
import interpreter

def run():
    messagebox.showinfo("Info", "Przycisk został naciśnięty!")

def print(name):
    with open(name + '.bf', 'r', encoding='utf-8') as file:
        code = file.read()
    return interpreter.interpreter(code)

root = tk.Tk()
root.title(print("title"))

button = tk.Button(root, text=print("button"), command=run, width=70, height=10)
button.pack(padx=20, pady=20)

root.mainloop()
