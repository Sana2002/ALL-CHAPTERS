# Using tkinter module develop Gui to ask the user to select shapes like oval, rectangle, square, and triangle and draw the shape using canvas.

import tkinter as tk
from tkinter import ttk
import math

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.shape_var = tk.StringVar()
        self.shape_var.set("Select Shape")

        shape_options = ["Select Shape", "Oval", "Rectangle", "Square", "Triangle"]
        shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var, values=shape_options)
        shape_dropdown.pack(pady=10)

        draw_button = tk.Button(root, text="Draw", command=self.draw_shape)
        draw_button.pack(pady=10)

    def draw_shape(self):
        selected_shape = self.shape_var.get()

        if selected_shape == "Oval":
            self.draw_oval()
        elif selected_shape == "Rectangle":
            self.draw_rectangle()
        elif selected_shape == "Square":
            self.draw_square()
        elif selected_shape == "Triangle":
            self.draw_triangle()

    def draw_oval(self):
        self.canvas.create_oval(50, 50, 200, 150, fill="blue")

    def draw_rectangle(self):
        self.canvas.create_rectangle(50, 50, 200, 150, fill="green")

    def draw_square(self):
        self.canvas.create_rectangle(50, 50, 150, 150, fill="red")

    def draw_triangle(self):
        # Draw a simple equilateral triangle
        side_length = 100
        height = math.sqrt(3) / 2 * side_length

        x1, y1 = 150, 50
        x2, y2 = x1 + side_length, y1
        x3, y3 = x1 + side_length / 2, y1 + height

        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="purple")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root)
    root.mainloop()

# ----------------------------Extention------------------------
    
import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.shape_var = tk.StringVar()
        self.shape_var.set("Select Shape")

        shape_options = ["Select Shape", "Oval", "Rectangle", "Square", "Triangle"]
        shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var, values=shape_options)
        shape_dropdown.pack(pady=10)

        self.coordinate_label = tk.Label(root, text="Enter Coordinates:")
        self.coordinate_label.pack()

        self.coordinate_entry = tk.Entry(root)
        self.coordinate_entry.pack(pady=5)

        draw_button = tk.Button(root, text="Draw", command=self.draw_shape)
        draw_button.pack(pady=10)

    def draw_shape(self):
        selected_shape = self.shape_var.get()
        coordinates = self.coordinate_entry.get()

        if selected_shape == "Select Shape":
            tk.messagebox.showwarning("Warning", "Please select a valid shape.")
            return

        try:
            coordinates = list(map(int, coordinates.split(',')))

            if selected_shape == "Oval":
                self.draw_oval(coordinates)
            elif selected_shape == "Rectangle":
                self.draw_rectangle(coordinates)
            elif selected_shape == "Square":
                self.draw_square(coordinates)
            elif selected_shape == "Triangle":
                self.draw_triangle(coordinates)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid coordinates. Please enter valid integer values.")

    def draw_oval(self, coordinates):
        if len(coordinates) == 4:
            self.canvas.create_oval(coordinates, fill="blue")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Oval.")

    def draw_rectangle(self, coordinates):
        if len(coordinates) == 4:
            self.canvas.create_rectangle(coordinates, fill="green")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Rectangle.")

    def draw_square(self, coordinates):
        if len(coordinates) == 4:
            self.canvas.create_rectangle(coordinates, fill="red")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Square.")

    def draw_triangle(self, coordinates):
        if len(coordinates) == 6:
            self.canvas.create_polygon(coordinates, fill="purple")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Triangle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root)
    root.mainloop()