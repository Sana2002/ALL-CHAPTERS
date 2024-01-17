# Create a GUI that takes input and changes all letters to upper case.
# hint : Use upper() function

import tkinter as tk

def convert_to_uppercase():
    input_text = entry_text.get()
    result.set(f"Converted text: {input_text.upper()}")

# Create the main window
root = tk.Tk()
root.title("Uppercase Converter")

# Create labels, entry widget, and button
label_text = tk.Label(root, text="Enter text:")
entry_text = tk.Entry(root)
result = tk.StringVar(value="")

label_result = tk.Label(root, textvariable=result)
button_convert = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)

# Place widgets using the Grid geometry manager
label_text.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_text.grid(row=0, column=1, padx=10, pady=10)
button_convert.grid(row=1, columnspan=2, pady=10)
label_result.grid(row=2, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
