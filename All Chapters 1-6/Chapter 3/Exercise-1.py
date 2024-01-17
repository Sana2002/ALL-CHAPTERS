# Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.

# In InputFrame, include the following:
# - A title label in blue.
# - An entry field for the user's name.
# - A dropdown menu for selecting a color.
# - An "Update Greeting" button.
# - In DisplayFrame, include a label to display the personalized greeting.
# - Initially, DisplayFrame is empty, when the user clicks the "Update Greeting" button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.
# Use different background colors for each frame.


import tkinter as tk
from tkinter import ttk

class GreetingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Greeting App")

        # Set background colors
        self.root.configure(bg='#F0F0F0')
        self.input_frame_bg_color = '#C0C0C0'
        self.display_frame_bg_color = '#E0E0E0'

        # Create InputFrame
        self.input_frame = tk.Frame(root, bg=self.input_frame_bg_color, padx=20, pady=20)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        # Add title label in blue
        title_label = tk.Label(self.input_frame, text="Greeting App", font=("Helvetica", 16, "bold"), fg="blue", bg=self.input_frame_bg_color)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Entry field for user's name
        name_label = tk.Label(self.input_frame, text="Your Name:", bg=self.input_frame_bg_color)
        name_label.grid(row=1, column=0, sticky='e')
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=1, column=1, padx=(0, 10))

        # Dropdown menu for selecting a color
        color_label = tk.Label(self.input_frame, text="Select Color:", bg=self.input_frame_bg_color)
        color_label.grid(row=2, column=0, sticky='e')
        self.color_var = tk.StringVar()
        color_choices = ['Red', 'Green', 'Blue', 'Yellow']
        self.color_dropdown = ttk.Combobox(self.input_frame, textvariable=self.color_var, values=color_choices)
        self.color_dropdown.grid(row=2, column=1, padx=(0, 10))

        # Update Greeting button
        update_button = tk.Button(self.input_frame, text="Update Greeting", command=self.update_greeting, bg='#90EE90')
        update_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        # Create DisplayFrame
        self.display_frame = tk.Frame(root, bg=self.display_frame_bg_color, padx=20, pady=20)
        self.display_frame.grid(row=0, column=1, padx=10, pady=10)

        # Label to display personalized greeting
        self.greeting_label = tk.Label(self.display_frame, text="", font=("Helvetica", 14), bg=self.display_frame_bg_color)
        self.greeting_label.pack()

    def update_greeting(self):
        name = self.name_entry.get()
        color = self.color_var.get()
        greeting_text = f"Hello, {name}! Welcome to the Greeting App!"
        self.greeting_label.config(text=greeting_text, fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = GreetingApp(root)
    root.mainloop()
