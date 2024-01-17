# squares, and rectangles. The application should utilize a tabbed interface to organize the calculations for each shape.
# Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.)

import tkinter as tk
from tkinter import ttk, messagebox
import math

class AreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")

        self.tabControl = ttk.Notebook(root)

        # Circle Tab
        self.circle_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.circle_tab, text="Circle")
        self.create_circle_tab()

        # Square Tab
        self.square_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.square_tab, text="Square")
        self.create_square_tab()

        # Rectangle Tab
        self.rectangle_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.rectangle_tab, text="Rectangle")
        self.create_rectangle_tab()

        self.tabControl.pack(expand=1, fill="both")

    def create_circle_tab(self):
        tk.Label(self.circle_tab, text="Radius:").grid(row=0, column=0, padx=10, pady=10)
        self.circle_radius_entry = tk.Entry(self.circle_tab)
        self.circle_radius_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.circle_tab, text="Calculate Area", command=self.calculate_circle_area)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_circle_area(self):
        try:
            radius = float(self.circle_radius_entry.get())
            if radius < 0:
                raise ValueError("Radius cannot be negative.")
            area = math.pi * radius**2
            messagebox.showinfo("Result", f"The area of the circle is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_square_tab(self):
        tk.Label(self.square_tab, text="Side Length:").grid(row=0, column=0, padx=10, pady=10)
        self.square_side_entry = tk.Entry(self.square_tab)
        self.square_side_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.square_tab, text="Calculate Area", command=self.calculate_square_area)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_square_area(self):
        try:
            side_length = float(self.square_side_entry.get())
            if side_length < 0:
                raise ValueError("Side length cannot be negative.")
            area = side_length**2
            messagebox.showinfo("Result", f"The area of the square is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_rectangle_tab(self):
        tk.Label(self.rectangle_tab, text="Length:").grid(row=0, column=0, padx=10, pady=10)
        self.rectangle_length_entry = tk.Entry(self.rectangle_tab)
        self.rectangle_length_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.rectangle_tab, text="Width:").grid(row=1, column=0, padx=10, pady=10)
        self.rectangle_width_entry = tk.Entry(self.rectangle_tab)
        self.rectangle_width_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.rectangle_tab, text="Calculate Area", command=self.calculate_rectangle_area)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_rectangle_area(self):
        try:
            length = float(self.rectangle_length_entry.get())
            width = float(self.rectangle_width_entry.get())
            if length < 0 or width < 0:
                raise ValueError("Length and width cannot be negative.")
            area = length * width
            messagebox.showinfo("Result", f"The area of the rectangle is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculator(root)
    root.mainloop()