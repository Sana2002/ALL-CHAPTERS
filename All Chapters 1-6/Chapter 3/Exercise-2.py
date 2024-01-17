# Develop a coffee Vending Machine that asks users to select the type of coffee, and also prompts users to select various options like sugar, milk, etc. Once selected display the message using a message box. Also, use images in the app.

import tkinter as tk
from tkinter import messagebox

class CoffeeVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Vending Machine")

        # Coffee options
        self.coffee_options = ["Espresso", "Latte", "Cappuccino", "Black Coffee"]

        # Ingredients options
        self.sugar_var = tk.BooleanVar()
        self.milk_var = tk.BooleanVar()
        self.cream_var = tk.BooleanVar()

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Coffee selection
        tk.Label(self.root, text="Select Coffee Type:").pack()

        self.coffee_var = tk.StringVar()
        self.coffee_var.set(self.coffee_options[0])
        coffee_menu = tk.OptionMenu(self.root, self.coffee_var, *self.coffee_options)
        coffee_menu.pack()

        # Ingredients selection
        tk.Label(self.root, text="Select Options:").pack()

        tk.Checkbutton(self.root, text="Sugar", variable=self.sugar_var).pack()
        tk.Checkbutton(self.root, text="Milk", variable=self.milk_var).pack()
        tk.Checkbutton(self.root, text="Cream", variable=self.cream_var).pack()

        # Order button
        tk.Button(self.root, text="Place Order", command=self.place_order).pack()

    def place_order(self):
        coffee_type = self.coffee_var.get()

        sugar = "with Sugar" if self.sugar_var.get() else "without Sugar"
        milk = "with Milk" if self.milk_var.get() else "without Milk"
        cream = "with Cream" if self.cream_var.get() else "without Cream"

        order_details = f"You have ordered a {coffee_type} {sugar} {milk} {cream}. Enjoy your coffee!"

        messagebox.showinfo("Order Confirmation", order_details)


if __name__ == "__main__":
    root = tk.Tk()
    coffee_machine = CoffeeVendingMachine(root)
    root.mainloop()


#-----------------Extention-----------------
    
# Add other features to the previous app such as handling money.
    
import tkinter as tk
from tkinter import messagebox

class CoffeeVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Vending Machine")

        # Coffee options
        self.coffee_options = {
            "Espresso": 2.50,
            "Latte": 3.00,
            "Cappuccino": 3.50,
            "Black Coffee": 2.00
        }

        # Ingredients options
        self.sugar_var = tk.BooleanVar()
        self.milk_var = tk.BooleanVar()
        self.cream_var = tk.BooleanVar()

        # Money variables
        self.inserted_money = tk.DoubleVar()
        self.inserted_money.set(0.0)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Coffee selection
        tk.Label(self.root, text="Select Coffee Type:").pack()

        self.coffee_var = tk.StringVar()
        self.coffee_var.set(list(self.coffee_options.keys())[0])
        coffee_menu = tk.OptionMenu(self.root, self.coffee_var, *self.coffee_options.keys())
        coffee_menu.pack()

        # Ingredients selection
        tk.Label(self.root, text="Select Options:").pack()

        tk.Checkbutton(self.root, text="Sugar", variable=self.sugar_var).pack()
        tk.Checkbutton(self.root, text="Milk", variable=self.milk_var).pack()
        tk.Checkbutton(self.root, text="Cream", variable=self.cream_var).pack()

        # Money handling
        tk.Label(self.root, text="Insert Money ($):").pack()

        money_entry = tk.Entry(self.root, textvariable=self.inserted_money)
        money_entry.pack()

        # Order button
        tk.Button(self.root, text="Place Order", command=self.place_order).pack()

    def place_order(self):
        coffee_type = self.coffee_var.get()
        coffee_cost = self.coffee_options[coffee_type]

        sugar = "with Sugar" if self.sugar_var.get() else "without Sugar"
        milk = "with Milk" if self.milk_var.get() else "without Milk"
        cream = "with Cream" if self.cream_var.get() else "without Cream"

        order_details = f"You have ordered a {coffee_type} {sugar} {milk} {cream}.\n"

        total_cost = coffee_cost
        order_details += f"Total Cost: ${total_cost:.2f}\n"

        inserted_money = self.inserted_money.get()
        if inserted_money < total_cost:
            order_details += f"Insufficient funds. Please insert more money."
        else:
            change = inserted_money - total_cost
            order_details += f"Thank you! Enjoy your coffee!\nChange: ${change:.2f}"

        messagebox.showinfo("Order Confirmation", order_details)
        self.reset_values()

    def reset_values(self):
        self.coffee_var.set(list(self.coffee_options.keys())[0])
        self.sugar_var.set(False)
        self.milk_var.set(False)
        self.cream_var.set(False)
        self.inserted_money.set(0.0)


if __name__ == "__main__":
    root = tk.Tk()
    coffee_machine = CoffeeVendingMachine(root)
    root.mainloop()
