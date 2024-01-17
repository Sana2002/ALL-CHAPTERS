# Develop a GUI using Tkinter to Create a class called Students.
# - The class should have the following members.```Name (string), Mark1 (int), Mark2 (int), Mark3 (int) ``` 
# - The class should have the following methods
# ```calcGrade()``` - should return an average from the three marks.```display()```- should output the student name and calculated grade average
# - Create one object using a constructor that contains parameters to initialize all of the variables
# - Ask user to input the variable values using input() and pass the values to the second object

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.Name = name
        self.Mark1 = mark1
        self.Mark2 = mark2
        self.Mark3 = mark3

    def calcGrade(self):
        average = (self.Mark1 + self.Mark2 + self.Mark3) / 3
        return average

    def display(self):
        return f"Student Name: {self.Name}\nAverage Grade: {self.calcGrade():.2f}"

class StudentsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information")

        self.create_widgets()

    def create_widgets(self):
        label_info = ttk.Label(self.root, text="Enter Student Information:")
        label_info.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = ttk.Label(self.root, text="Name:")
        label_name.grid(row=1, column=0, pady=5, sticky=tk.W)
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.grid(row=1, column=1, pady=5)

        label_mark1 = ttk.Label(self.root, text="Mark 1:")
        label_mark1.grid(row=2, column=0, pady=5, sticky=tk.W)
        self.entry_mark1 = ttk.Entry(self.root)
        self.entry_mark1.grid(row=2, column=1, pady=5)

        label_mark2 = ttk.Label(self.root, text="Mark 2:")
        label_mark2.grid(row=3, column=0, pady=5, sticky=tk.W)
        self.entry_mark2 = ttk.Entry(self.root)
        self.entry_mark2.grid(row=3, column=1, pady=5)

        label_mark3 = ttk.Label(self.root, text="Mark 3:")
        label_mark3.grid(row=4, column=0, pady=5, sticky=tk.W)
        self.entry_mark3 = ttk.Entry(self.root)
        self.entry_mark3.grid(row=4, column=1, pady=5)

        calculate_button = ttk.Button(self.root, text="Calculate and Display", command=self.calculate_and_display)
        calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_and_display(self):
        try:
            name = self.entry_name.get()
            mark1 = float(self.entry_mark1.get())
            mark2 = float(self.entry_mark2.get())
            mark3 = float(self.entry_mark3.get())

            student1 = Students("John Doe", 90, 85, 88)  # Initializing using constructor
            student2 = Students(name, mark1, mark2, mark3)  # Initializing using user input

            display_message = student1.display() + "\n\n" + student2.display()
            tk.messagebox.showinfo("Student Information", display_message)

        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numerical values for marks.")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentsApp(root)
    root.mainloop()
