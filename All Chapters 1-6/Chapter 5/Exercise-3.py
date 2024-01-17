# Develop a GUI using Tkinter to Create an employee class with the following members:
#  ```name, age, id, salary```
# - Add the following methods:
# ```setData()``` - should allow employee data to be set via user input,```getData()```- should output employee data to the console
# - Create a list of 5 employees. Ask the user to enter the details of 5 employees using the add_employee method and then display the output using the display_emloyee method as mentioned below
# Expected output:
# ```			
# Name	Position	Salary	ID
# Alice	Manager		9500.0	1
# Bob	Accountant	6000.0	2
# Brain	Social Media	4000.0	3
# Frank	Salesman	2500.0	4
# Marker	Clerk		1500.0	5
# ```

import tkinter as tk
from tkinter import ttk

class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0

    def setData(self, name, position, salary, employee_id):
        self.name = name
        self.position = position
        self.salary = float(salary)
        self.id = int(employee_id)

    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Information")

        self.employee_list = []
        self.current_index = 0

        self.create_widgets()

    def create_widgets(self):
        label_info = ttk.Label(self.root, text="Enter Employee Information:")
        label_info.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = ttk.Label(self.root, text="Name:")
        label_name.grid(row=1, column=0, pady=5, sticky=tk.W)
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.grid(row=1, column=1, pady=5)

        label_position = ttk.Label(self.root, text="Position:")
        label_position.grid(row=2, column=0, pady=5, sticky=tk.W)
        self.entry_position = ttk.Entry(self.root)
        self.entry_position.grid(row=2, column=1, pady=5)

        label_salary = ttk.Label(self.root, text="Salary:")
        label_salary.grid(row=3, column=0, pady=5, sticky=tk.W)
        self.entry_salary = ttk.Entry(self.root)
        self.entry_salary.grid(row=3, column=1, pady=5)

        label_id = ttk.Label(self.root, text="ID:")
        label_id.grid(row=4, column=0, pady=5, sticky=tk.W)
        self.entry_id = ttk.Entry(self.root)
        self.entry_id.grid(row=4, column=1, pady=5)

        add_button = ttk.Button(self.root, text="Add Employee", command=self.add_employee)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

        display_button = ttk.Button(self.root, text="Display Employees", command=self.display_employees)
        display_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_employee(self):
        name = self.entry_name.get()
        position = self.entry_position.get()
        salary = self.entry_salary.get()
        employee_id = self.entry_id.get()

        employee = Employee()
        employee.setData(name, position, salary, employee_id)
        self.employee_list.append(employee)

        self.entry_name.delete(0, tk.END)
        self.entry_position.delete(0, tk.END)
        self.entry_salary.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)

    def display_employees(self):
        print("Name\tPosition\tSalary\tID")
        for employee in self.employee_list:
            print(employee.getData())


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
