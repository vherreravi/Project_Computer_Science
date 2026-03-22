"""
=============================================
  🧮  Simple Calculator
  Beginner Python + Tkinter GUI
=============================================

YOUR JOB as a student:
  - Complete the functions in the "STUDENT SECTION" below
  - Do NOT modify anything in the "GUI SECTION"
  - Test each function one at a time!

Run this file with:  python calculator_project.py
"""

import tkinter as tk
from tkinter import messagebox


# ============================================================
#  ✏️  STUDENT SECTION — Write your functions here!
# ============================================================

def add(a, b):
    """
    Add two numbers together and return the result.

    Example:
        add(3, 4)  →  7
        add(10, 5) →  15

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


def subtract(a, b):
    """
    Subtract b from a and return the result.

    Example:
        subtract(10, 4) →  6
        subtract(3, 7)  → -4

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Example:
        multiply(3, 4)  → 12
        multiply(5, 0)  →  0

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


def divide(a, b):
    """
    Divide a by b and return the result.
    IMPORTANT: If b is 0, return the string "Error: Cannot divide by zero"

    Example:
        divide(10, 2)  →  5.0
        divide(7, 0)   →  "Error: Cannot divide by zero"

    HINT: Use an if/else statement to check if b == 0

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


# ============================================================
#  🖥️  GUI SECTION — Do not edit below this line!
#       (But feel free to read and explore how it works)
# ============================================================

def calculate(num1_entry, num2_entry, operation_var, result_label):
    """Reads inputs, calls the student's functions, and shows the result."""
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")
        return

    op = operation_var.get()

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "×":
        result = multiply(a, b)
    elif op == "÷":
        result = divide(a, b)
    else:
        result = "Select an operation"

    if result is None:
        messagebox.showwarning(
            "Function Not Done",
            f"Your '{op}' function returned None.\nMake sure you used 'return' in your function!"
        )
        result_label.config(text="= ???", fg="#e74c3c")
    else:
        result_label.config(text=f"= {result}", fg="#2ecc71")


def build_gui():
    """Build and launch the calculator window."""
    window = tk.Tk()
    window.title("🧮 Student Calculator")
    window.geometry("380x340")
    window.configure(bg="#1e1e2e")
    window.resizable(False, False)

    # Title
    tk.Label(
        window, text="Student Calculator", font=("Courier", 16, "bold"),
        bg="#1e1e2e", fg="#cdd6f4"
    ).pack(pady=(18, 4))

    tk.Label(
        window, text="Fill in the functions to make this work!",
        font=("Courier", 9), bg="#1e1e2e", fg="#6c7086"
    ).pack(pady=(0, 14))

    # Input frame
    frame = tk.Frame(window, bg="#313244", padx=16, pady=16)
    frame.pack(padx=20, fill="x")

    tk.Label(frame, text="First Number:", font=("Courier", 10),
             bg="#313244", fg="#cdd6f4").grid(row=0, column=0, sticky="w")
    num1_entry = tk.Entry(frame, font=("Courier", 12), width=12,
                          bg="#45475a", fg="#cdd6f4", insertbackground="white",
                          relief="flat", bd=4)
    num1_entry.grid(row=0, column=1, padx=(8, 0), pady=4)

    tk.Label(frame, text="Second Number:", font=("Courier", 10),
             bg="#313244", fg="#cdd6f4").grid(row=1, column=0, sticky="w")
    num2_entry = tk.Entry(frame, font=("Courier", 12), width=12,
                          bg="#45475a", fg="#cdd6f4", insertbackground="white",
                          relief="flat", bd=4)
    num2_entry.grid(row=1, column=1, padx=(8, 0), pady=4)

    tk.Label(frame, text="Operation:", font=("Courier", 10),
             bg="#313244", fg="#cdd6f4").grid(row=2, column=0, sticky="w")
    operation_var = tk.StringVar(value="+")
    op_menu = tk.OptionMenu(frame, operation_var, "+", "-", "×", "÷")
    op_menu.config(font=("Courier", 12), bg="#45475a", fg="#cdd6f4",
                   activebackground="#585b70", relief="flat", bd=0)
    op_menu.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=4)

    # Result label
    result_label = tk.Label(
        window, text="= ?", font=("Courier", 22, "bold"),
        bg="#1e1e2e", fg="#89b4fa"
    )
    result_label.pack(pady=16)

    # Calculate button
    tk.Button(
        window, text="Calculate →",
        font=("Courier", 12, "bold"),
        bg="#89b4fa", fg="#1e1e2e",
        activebackground="#b4befe",
        relief="flat", bd=0, padx=16, pady=8,
        cursor="hand2",
        command=lambda: calculate(num1_entry, num2_entry, operation_var, result_label)
    ).pack()

    window.mainloop()


# Entry point
if __name__ == "__main__":
    build_gui()
