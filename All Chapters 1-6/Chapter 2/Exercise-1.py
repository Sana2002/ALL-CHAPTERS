# Develop a GUI program to do the following using the tkinter module
# - create a label to display the welcome message and change the label font style (font name, bold, size)
# - Set the default window size
# - Disable resizing the window
# - Add background color to the Window.

import tkinter as tk
from tkinter import font

def change_font():
    custom_font = font.Font(family="Arial", size=16, weight="bold")
    welcome_label.config(font=custom_font)

# Create the main window
root = tk.Tk()
root.title("Welcome GUI Program")

# Set the default window size
root.geometry("400x200")

# Disable resizing the window
root.resizable(False, False)

# Add background color to the window
root.configure(bg="#e6e6e6")

# Create and place a label
welcome_label = tk.Label(root, text="Welcome to GUI Programming!", font=("Helvetica", 14), bg="#e6e6e6")
welcome_label.pack(pady=20)

# Button to change font
change_font_button = tk.Button(root, text="Change Font", command=change_font)
change_font_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
