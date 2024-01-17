import tkinter as tk
from tkinter import filedialog, messagebox

class PetrolCalculatorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Petrol Calculator App")

        self.create_widgets()

    def create_widgets(self):
        # Button to open file dialog and calculate results
        tk.Button(self.root, text="Open File", command=self.calculate_results).pack(pady=20)

        # Labels to display results
        self.cost_label = tk.Label(self.root, text="Cost of petrol per liter: ")
        self.cost_label.pack()

        self.average_label = tk.Label(self.root, text="Overall average price per liter: ")
        self.average_label.pack()

        self.under_3_5_label = tk.Label(self.root, text="Petrol bought at under 3.5 AED per liter: ")
        self.under_3_5_label.pack()

    def calculate_results(self):
        try:
            # Use file dialog to select the petrolPrice.txt file
            file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

            # Read data from the file and perform calculations
            liters_list = []
            cost_list = []

            with open(file_name, "r") as file:
                # Skip the header line
                next(file)
                
                for line in file:
                    liters, cost = map(float, line.strip().split("\t"))
                    liters_list.append(liters)
                    cost_list.append(cost)

            # Calculate results
            total_cost = sum(cost_list)
            total_liters = sum(liters_list)
            cost_per_liter = total_cost / total_liters
            average_price_per_liter = sum(cost_list) / len(cost_list)
            under_3_5_liters = sum(1 for cost in cost_list if cost / liters_list[cost_list.index(cost)] < 3.5)

            # Display results in labels
            self.cost_label.config(text=f"Cost of petrol per liter: {cost_per_liter:.2f} AED")
            self.average_label.config(text=f"Overall average price per liter: {average_price_per_liter:.2f} AED")
            self.under_3_5_label.config(text=f"Petrol bought at under 3.5 AED per liter: {under_3_5_liters} liters")

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found. Please select a valid file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "_main_":
    root = tk.Tk()
    app = PetrolCalculatorApp(root)
    root.mainloop()
#Make petrolPrice.txt