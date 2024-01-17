# Develop a GUI using Tkinter to calculate the area of Shapes.
# Create a parent class called Shape. This should have the following methods
# ```inputSides()``` – Ask the user to enter the sides of the shape. Now create subclasses for a circle, rectangle, and triangle. These should include an appropriate ``` area()``` method that will use the side values from the shape class.

import tkinter as tk
from tkinter import ttk, messagebox
import math

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass  # To be implemented in subclasses

    def area(self):
        pass  # To be implemented in subclasses

class Circle(Shape):
    def inputSides(self):
        radius = float(self.entry_radius.get())
        self.sides = [radius]

    def area(self):
        return math.pi * self.sides[0] ** 2

class Rectangle(Shape):
    def inputSides(self):
        length = float(self.entry_length.get())
        width = float(self.entry_width.get())
        self.sides = [length, width]

    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def inputSides(self):
        side1 = float(self.entry_side1.get())
        side2 = float(self.entry_side2.get())
        side3 = float(self.entry_side3.get())
        self.sides = [side1, side2, side3]

    def area(self):
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

class ShapeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Area Calculator")

        self.create_widgets()

    def create_widgets(self):
        label_info = ttk.Label(self.root, text="Select Shape and Enter Dimensions:")
        label_info.grid(row=0, column=0, columnspan=2, pady=10)

        shape_var = tk.StringVar()
        shape_options = ["Select Shape", "Circle", "Rectangle", "Triangle"]
        shape_dropdown = ttk.Combobox(self.root, textvariable=shape_var, values=shape_options)
        shape_dropdown.grid(row=1, column=0, pady=5)

        self.shapes = {"Circle": Circle(), "Rectangle": Rectangle(), "Triangle": Triangle()}

        self.create_input_fields()

        calculate_button = ttk.Button(self.root, text="Calculate Area", command=self.calculate_area)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def create_input_fields(self):
        self.entry_radius = self.create_entry_field("Radius:", row=2)
        self.entry_length = self.create_entry_field("Length:", row=2)
        self.entry_width = self.create_entry_field("Width:", row=3)
        self.entry_side1 = self.create_entry_field("Side 1:", row=2)
        self.entry_side2 = self.create_entry_field("Side 2:", row=3)
        self.entry_side3 = self.create_entry_field("Side 3:", row=4)

    def create_entry_field(self, label_text, row):
        label = ttk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, pady=5, sticky=tk.W)

        entry = ttk.Entry(self.root)
        entry.grid(row=row, column=1, pady=5)
        return entry

    def calculate_area(self):
        shape_type = self.shapes.get(self.shapes_var.get())

        if shape_type is None:
            messagebox.showwarning("Warning", "Please select a valid shape.")
            return

        shape_type.inputSides()

        try:
            area = shape_type.area()
            messagebox.showinfo("Result", f"The area of the {self.shapes_var.get()} is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeCalculatorApp(root)
    root.mainloop()
