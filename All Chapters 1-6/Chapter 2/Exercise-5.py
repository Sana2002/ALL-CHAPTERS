# Develop a GUI to perform basic arithmetic operations like addition, subtraction, multiplication, Division, and modulo division using buttons. You can ask the user to enter the values in entry widget and select the operation to be performed.

import tkinter as tk

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation.get() == "Addition":
            result.set(num1 + num2)
        elif operation.get() == "Subtraction":
            result.set(num1 - num2)
        elif operation.get() == "Multiplication":
            result.set(num1 * num2)
        elif operation.get() == "Division":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Cannot divide by zero")
        elif operation.get() == "Modulo":
            if num2 != 0:
                result.set(num1 % num2)
            else:
                result.set("Cannot calculate modulo with zero")
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Arithmetic Operations Calculator")

# Create labels, entry widgets, and buttons
label_num1 = tk.Label(root, text="Number 1:")
label_num2 = tk.Label(root, text="Number 2:")
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
operation = tk.StringVar(value="Addition")  # Default operation is Addition
result = tk.StringVar(value="Result: ")

label_result = tk.Label(root, textvariable=result)

button_add = tk.Button(root, text="Addition", command=perform_operation)
button_subtract = tk.Button(root, text="Subtraction", command=perform_operation)
button_multiply = tk.Button(root, text="Multiplication", command=perform_operation)
button_divide = tk.Button(root, text="Division", command=perform_operation)
button_modulo = tk.Button(root, text="Modulo", command=perform_operation)

# Place widgets using the Grid geometry manager
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_num1.grid(row=0, column=1, padx=10, pady=10)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

button_add.grid(row=2, column=0, pady=10)
button_subtract.grid(row=2, column=1, pady=10)
button_multiply.grid(row=3, column=0, pady=10)
button_divide.grid(row=3, column=1, pady=10)
button_modulo.grid(row=4, column=0, pady=10)

label_result.grid(row=5, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
