# Use this exercise to play around with creating and accessing class members and methods. Develop a GUI using Tkinter to Create a class called Animal
# - Give the class at least the following members  ```Type, Name, Colour, Age, Weight, Noise```
# - The class should have the following methods
# ```sayHello()``` - says its name via print,```makeNoise()``` -make an appropriate noise via print, ```animalDetails()``` -output all the details of the animal object
# - Instantiate at least two objects from your animal class (e.g. Dog, Cow)
# - Set values for each of the variables
# - Invoke each of the class functions

import tkinter as tk
from tkinter import ttk, messagebox

class Animal:
    def __init__(self, type, name, color, age, weight, noise):
        self.Type = type
        self.Name = name
        self.Colour = color
        self.Age = age
        self.Weight = weight
        self.Noise = noise

    def sayHello(self):
        print(f"{self.Type} {self.Name} says: Hello!")

    def makeNoise(self):
        print(f"{self.Type} {self.Name} makes a {self.Noise} noise.")

    def animalDetails(self):
        print(f"Animal Details:\nType: {self.Type}\nName: {self.Name}\nColor: {self.Colour}\nAge: {self.Age}\nWeight: {self.Weight}\nNoise: {self.Noise}")

class AnimalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Information")

        self.create_widgets()

    def create_widgets(self):
        dog_button = ttk.Button(self.root, text="Dog", command=self.create_dog)
        dog_button.grid(row=0, column=0, padx=10, pady=10)

        cow_button = ttk.Button(self.root, text="Cow", command=self.create_cow)
        cow_button.grid(row=0, column=1, padx=10, pady=10)

    def create_dog(self):
        dog = Animal("Dog", "Buddy", "Brown", 3, 15, "Woof")
        self.display_animal_info(dog)

    def create_cow(self):
        cow = Animal("Cow", "Mooey", "Black and White", 5, 500, "Moo")
        self.display_animal_info(cow)

    def display_animal_info(self, animal):
        animal.sayHello()
        animal.makeNoise()
        animal.animalDetails()


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimalApp(root)
    root.mainloop()
