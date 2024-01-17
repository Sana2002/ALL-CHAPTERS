# Create a login page using the Grid geometry.

import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are correct (you can replace this with your authentication logic)
    if username == "user" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create labels, entry widgets, and login button
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Show '*' for password entry
button_login = tk.Button(root, text="Login", command=login)

# Place widgets using the Grid geometry manager
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_login.grid(row=2, column=1, pady=10)

# Run the Tkinter event loop
root.mainloop()
