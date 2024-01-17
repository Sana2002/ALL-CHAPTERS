# Develop a GUI to perform Arithmetic Operations.
# - Create a class ArithmeticOperations with the following
# - a result variable to store the result after calculation
# - a function Calculate() - To perform an arithmetic operation selected by the user.
# - You can use Combobox to provide users with options to perform selected arithmetic operations and entry widgets for the values.

import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "Addition":
                self.result = num1 + num2
            elif operation == "Subtraction":
                self.result = num1 - num2
            elif operation == "Multiplication":
                self.result = num1 * num2
            elif operation == "Division":
                if num2 != 0:
                    self.result = num1 / num2
                else:
                    raise ValueError("Cannot divide by zero.")
        except ValueError as e:
            return str(e)

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Calculator")

        self.arithmetic_operations = ArithmeticOperations()

        self.create_widgets()

    def create_widgets(self):
        label_info = ttk.Label(self.root, text="Arithmetic Calculator:")
        label_info.grid(row=0, column=0, columnspan=2, pady=10)

        label_operation = ttk.Label(self.root, text="Select Operation:")
        label_operation.grid(row=1, column=0, pady=5, sticky=tk.W)

        operation_var = tk.StringVar()
        operation_options = ["Addition", "Subtraction", "Multiplication", "Division"]
        operation_dropdown = ttk.Combobox(self.root, textvariable=operation_var, values=operation_options)
        operation_dropdown.grid(row=1, column=1, pady=5)

        label_num1 = ttk.Label(self.root, text="Enter Number 1:")
        label_num1.grid(row=2, column=0, pady=5, sticky=tk.W)

        entry_num1 = ttk.Entry(self.root)
        entry_num1.grid(row=2, column=1, pady=5)

        label_num2 = ttk.Label(self.root, text="Enter Number 2:")
        label_num2.grid(row=3, column=0, pady=5, sticky=tk.W)

        entry_num2 = ttk.Entry(self.root)
        entry_num2.grid(row=3, column=1, pady=5)

        calculate_button = ttk.Button(self.root, text="Calculate", command=lambda: self.calculate(operation_var.get(), entry_num1.get(), entry_num2.get()))
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        result_label = ttk.Label(self.root, text="Result:")
        result_label.grid(row=5, column=0, pady=5, sticky=tk.W)

        self.result_var = tk.StringVar()
        result_entry = ttk.Entry(self.root, textvariable=self.result_var, state="readonly")
        result_entry.grid(row=5, column=1, pady=5)

    def calculate(self, operation, num1, num2):
        result = self.arithmetic_operations.calculate(operation, num1, num2)
        if result is not None:
            self.result_var.set(result)
        else:
            self.result_var.set("Invalid input")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
