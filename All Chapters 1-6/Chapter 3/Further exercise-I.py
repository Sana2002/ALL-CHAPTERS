# Redo the vending machine app developed by you in Codelab-I using the tkinter module

import tkinter as tk
from tkinter import messagebox

class VendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")

        self.items = {
            "Kinza Cola": 1.50,
            "Oman chips": 1.00,
            "Mudhish Chips": 1.25,
            "Melco juice": 2.00
        }

        self.selected_item = tk.StringVar()
        self.selected_item.set("Select Item")

        self.create_widgets()

    def create_widgets(self):
        # Item selection dropdown
        item_label = tk.Label(self.root, text="Select Item:")
        item_label.grid(row=0, column=0, pady=10)

        item_dropdown = tk.OptionMenu(self.root, self.selected_item, *self.items.keys())
        item_dropdown.grid(row=0, column=1, pady=10)

        # Display price label
        price_label = tk.Label(self.root, text="Price:")
        price_label.grid(row=1, column=0)

        self.price_display = tk.Label(self.root, text="")
        self.price_display.grid(row=1, column=1)

        # Buy button
        buy_button = tk.Button(self.root, text="Buy", command=self.buy_item)
        buy_button.grid(row=2, column=0, columnspan=2, pady=10)

    def buy_item(self):
        item_name = self.selected_item.get()

        if item_name == "Select Item":
            messagebox.showinfo("Error", "Please select an item.")
        else:
            price = self.items[item_name]
            messagebox.showinfo("Purchase", f"You bought {item_name} for ${price:.2f}.")

            # Optionally, you can perform additional actions here, such as updating inventory or handling payment.

            # Reset the selection
            self.selected_item.set("Select Item")
            self.price_display.config(text="")

    def update_price(self, *args):
        item_name = self.selected_item.get()

        if item_name != "Select Item":
            price = self.items[item_name]
            self.price_display.config(text=f"${price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    vending_machine = VendingMachine(root)
    root.mainloop()