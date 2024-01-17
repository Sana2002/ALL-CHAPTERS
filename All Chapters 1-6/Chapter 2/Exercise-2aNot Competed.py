# Create a GUI with 4 labels using the pack() geometry as shown in the below images. The	first image on the left shows	the	original display and the	second image on right shows	what	happens	when	the	window	is	resized.

from tkinter import *
import tkinter as tk
root = Tk()
root.title("Resizeable Labels")
root.geometry("400x500")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH,expand=TRUE)

#Create four labels and pack them 
label_1 = tk.Label(frame,text="Label 1",bg="red")
label_2 = tk.Label(frame,text="Label 2",bg="green")
label_3 = tk.Label(frame,text="Label 3",bg="blue")
label_4 = tk.Label(frame,text="Label 4",bg="yellow")

label_1.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)
label_2.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)
label_3.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)
label_4.pack(side=tk.LEFT,fill=tk.BOTH,expand=TRUE)

root.mainloop()

#------------------------ADDITIONAL INFO------------------------

# Arguments values for many widgets, including Frames for Borders and Background 
# - bd is used for border width. For example bd=5
# - Relief is used for border-style values are FLAT, RAISED, GROOVE, SUNKEN, and RIDGE. For example relief=RAISED
# - bg is used for background color.For example bg="white" or bg="#FFFFFF".

# Pack arguments
# - Fill: Fill the space with the widget, Values are  Y, X, BOTH. For example fill=Y
# - Expand: The size of the button is expanded if the window is maximized. Values are 0,1, any number, YES, NO. For example  expand=0 (default) no expansion

import tkinter as tk

def on_resize(event):
    label1.config(text=f"Width: {event.width}")
    label2.config(text=f"Height: {event.height}")

# Create the main window
root = tk.Tk()
root.title("Resizable GUI")

# Create labels
label1 = tk.Label(root, text="Label 1", bd=5, relief="groove", bg="lightblue")
label2 = tk.Label(root, text="Label 2", bd=5, relief="groove", bg="lightgreen")
label3 = tk.Label(root, text="Label 3", bd=5, relief="groove", bg="lightcoral")
label4 = tk.Label(root, text="Label 4", bd=5, relief="groove", bg="lightgoldenrodyellow")

# Pack labels
label1.pack(fill="both", expand=True, side="left")
label2.pack(fill="both", expand=True, side="left")
label3.pack(fill="both", expand=True, side="left")
label4.pack(fill="both", expand=True, side="left")

# Bind the resize event
root.bind("<Configure>", on_resize)

# Run the Tkinter event loop
root.mainloop()
