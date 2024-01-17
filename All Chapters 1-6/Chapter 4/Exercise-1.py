import tkinter as tk
from tkinter import messagebox

class BioApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Bio Information App")

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Label(self.root, text="Age:").grid(row=1, column=0, sticky="e")
        tk.Label(self.root, text="Hometown:").grid(row=2, column=0, sticky="e")

        # Entry widgets
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1)

        self.hometown_entry = tk.Entry(self.root)
        self.hometown_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(self.root, text="Save to File", command=self.save_to_file).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Read from File", command=self.read_from_file).grid(row=4, column=0, columnspan=2, pady=10)

    def save_to_file(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        hometown = self.hometown_entry.get()

        try:
            with open("bio.txt", "w") as file:
                file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")
            messagebox.showinfo("Success", "Data saved to bio.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {e}")

    def read_from_file(self):
        try:
            with open("bio.txt", "r") as file:
                data = file.read()
            messagebox.showinfo("Bio Information", data)
        except FileNotFoundError:
            messagebox.showinfo("File Not Found", "bio.txt not found. Save data first.")

if __name__ == "_main_":
    root = tk.Tk()
    app = BioApp(root)
    root.mainloop()