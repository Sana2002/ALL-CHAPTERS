# Develop a GUI using Tkinter with a class that defines the characteristics of a dog. The program should instantiate two objects from this class and assign data to its members.
# The program should then output the data from each object and the oldest dog should woof via a class method.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return "Woof!"

    @classmethod
    def oldest_dog_bark(cls, dog1, dog2):
        oldest_dog = dog1 if dog1.age > dog2.age else dog2
        return f"The oldest dog, {oldest_dog.name}, says: {oldest_dog.bark()}"

class DogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dog Information")

        self.dog1 = Dog("Buddy", 3, "Labrador")
        self.dog2 = Dog("Charlie", 5, "Golden Retriever")

        self.create_widgets()

    def create_widgets(self):
        label_dog1 = ttk.Label(self.root, text="Dog 1 Information:")
        label_dog1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        label_dog2 = ttk.Label(self.root, text="Dog 2 Information:")
        label_dog2.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        dog1_info = f"Name: {self.dog1.name}\nAge: {self.dog1.age}\nBreed: {self.dog1.breed}"
        dog2_info = f"Name: {self.dog2.name}\nAge: {self.dog2.age}\nBreed: {self.dog2.breed}"

        label_dog1_info = ttk.Label(self.root, text=dog1_info)
        label_dog1_info.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        label_dog2_info = ttk.Label(self.root, text=dog2_info)
        label_dog2_info.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        bark_button = ttk.Button(self.root, text="Oldest Dog Bark", command=self.oldest_dog_bark)
        bark_button.grid(row=2, column=0, columnspan=2, pady=10)

    def oldest_dog_bark(self):
        bark_message = Dog.oldest_dog_bark(self.dog1, self.dog2)
        messagebox.showinfo("Oldest Dog Bark", bark_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = DogApp(root)
    root.mainloop()
