# - With	the	pack	layout	manager, Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame
# - Using Pack() align  A and C at the top and B and D at the bottom of the frames that contain them
# - Support	resizing. Use	the	‘expand’ and	‘fill’ attributes	of	the	pack	method	to	make	the	labels	grow	and	expand	into	the	available	space.
# - Assign border value as 5 to the frames

import tkinter as tk
from tkinter import Label

def on_resize(event):
    label_a.config(text=f"Width: {event.width}")
    label_b.config(text=f"Height: {event.height}")

# Create the main window
root = tk.Tk()
root.title("Resizable GUI with Pack")

# Create frames
left_frame = tk.Frame(root, bd=5, relief="groove")
right_frame = tk.Frame(root, bd=5, relief="groove")

# Create labels
label_a = tk.Label(left_frame, text="Label A", bg="lightblue") 
label_b = tk.Label(left_frame, text="Label B", bg="lightgreen")
label_c = tk.Label(right_frame, text="Label C", bg="lightcoral")
label_d = tk.Label(right_frame, text="Label D", bg="lightgoldenrodyellow")

# Pack labels inside frames
label_a.pack(side="top", expand=True, fill="both")
label_b.pack(side="bottom", expand=True, fill="both")
label_c.pack(side="top", expand=True, fill="both")
label_d.pack(side="bottom", expand=True, fill="both")

# Pack frames inside the main window
left_frame.pack(side="left", expand=True, fill="both")
right_frame.pack(side="right", expand=True, fill="both")

# Bind the resize event
root.bind("<Configure>", on_resize)

# Run the Tkinter event loop
root.mainloop()
