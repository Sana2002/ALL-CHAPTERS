import tkinter as tk
from tkinter import filedialog, messagebox

class CharCounterApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Character Counter App")

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for the character input
        tk.Label(self.root, text="Enter a character:").grid(row=0, column=0, sticky="e")
        self.char_entry = tk.Entry(self.root)
        self.char_entry.grid(row=0, column=1, columnspan=2)

        # Button to perform the counting
        tk.Button(self.root, text="Count Occurrences", command=self.count_occurrences).grid(row=1, column=0, columnspan=3, pady=10)

    def count_occurrences(self):
        char_to_count = self.char_entry.get()

        if not char_to_count:
            messagebox.showwarning("Warning", "Please enter a character.")
            return

        try:
            # Use file dialog to select the sentences.txt file
            file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

            with open(file_name, "r") as file:
                content = file.read()

            # Count occurrences of the specified character
            count = content.count(char_to_count)

            messagebox.showinfo("Result", f"The character '{char_to_count}' appears {count} times.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found. Please select a valid file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "_main_":
    root = tk.Tk()
    app = CharCounterApp(root)
    root.mainloop()