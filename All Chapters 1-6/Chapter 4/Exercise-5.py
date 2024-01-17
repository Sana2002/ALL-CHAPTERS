import tkinter as tk
from tkinter import messagebox

class PasswordCheckerApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Checker App")

        # Initialize attempts counter
        self.attempts = 0
        self.max_attempts = 5

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for the password input
        tk.Label(self.root, text="Enter Password:").grid(row=0, column=0, sticky="e")
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=0, column=1, columnspan=2)

        # Button to check the password
        tk.Button(self.root, text="Check Password", command=self.check_password).grid(row=1, column=0, columnspan=3, pady=10)

    def check_password(self):
        # Get the entered password
        password = self.password_entry.get()

        # Password criteria
        lowercase = any(char.islower() for char in password)
        uppercase = any(char.isupper() for char in password)
        digit = any(char.isdigit() for char in password)
        special_char = any(char in "$#@!" for char in password)
        length = 6 <= len(password) <= 12

        # Check if password meets the criteria
        if lowercase and uppercase and digit and special_char and length:
            messagebox.showinfo("Password Valid", "Password is valid!")
            self.root.destroy()  # Close the app after successful validation
        else:
            self.attempts += 1
            remaining_attempts = self.max_attempts - self.attempts

            if remaining_attempts > 0:
                messagebox.showwarning("Invalid Password", f"Password is invalid. {remaining_attempts} attempts remaining.")
            else:
                messagebox.showerror("Alert", "The authorities have been alerted! Too many failed attempts.")
                self.root.destroy()  # Close the app after 5 failed attempts

if __name__ == "_main_":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()