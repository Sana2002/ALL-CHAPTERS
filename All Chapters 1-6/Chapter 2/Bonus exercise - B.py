# Create a program to take input of the user's date of birth and output the age.
# Expected input: 8/5/2018
# Expected output: Your age is 5 years
# Hint: you can use the date from datetime package to get today's date

from datetime import datetime
import tkinter as tk

def calculate_age():
    try:
        dob_str = entry_dob.get()
        dob = datetime.strptime(dob_str, "%m/%d/%Y")
        today = datetime.now()

        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        result.set(f"Your age is {age} years")
    except ValueError:
        result.set("Invalid date format")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create labels, entry widget, and button
label_dob = tk.Label(root, text="Enter your Date of Birth (MM/DD/YYYY):")
entry_dob = tk.Entry(root)
result = tk.StringVar(value="")

label_result = tk.Label(root, textvariable=result)
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)

# Place widgets using the Grid geometry manager
label_dob.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_dob.grid(row=0, column=1, padx=10, pady=10)
button_calculate.grid(row=1, columnspan=2, pady=10)
label_result.grid(row=2, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
