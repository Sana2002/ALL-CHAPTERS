# Chapter 3 - Exercises
Exercises under the heading **Assessment Exercises** with a ☑️ must be attempted as a minimum expectation of the programming skills portfolio assessment. The assessment exercises also include some bonus exercises, solving these bonus exercises offers the potential to attain marks in the higher grade boundaries.

Further exercises are provided for you to practice and develop your programming skills. Completing these exercises is encouraged, although they have **no impact** on the programming skills portfolio mark.
For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository. Once you have completed your solution you should make sure you commit and push the code to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.

---

&nbsp;
## Assessment Exercises
### Exercise 1: Greeting App ☑️
Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.

In InputFrame, include the following:
- A title label in blue.
- An entry field for the user's name.
- A dropdown menu for selecting a color.
- An "Update Greeting" button.
- In DisplayFrame, include a label to display the personalized greeting.
- Initially, DisplayFrame is empty, when the user clicks the "Update Greeting" button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.

Use different background colors for each frame.

&nbsp;
&nbsp;
### Exercise 2: Coffee Vending Machine☑️
Develop a coffee Vending Machine that asks users to select the type of coffee, and also prompts users to select various options like sugar, milk, etc. Once selected display the message using a message box. Also, use images in the app.
&nbsp;
### Extension :
Add other features to the previous app such as handling money.

&nbsp;
&nbsp;

------------------------------------------------------------------------------------------------------------------------------------------
## Exercise 3: Area Function☑️
Develop a GUI application using tkinter that allows users to calculate and display the areas of various shapes, including circles, squares, and rectangles. The application should utilize a tabbed interface to organize the calculations for each shape.
Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.)

<!-- import tkinter as tk
from tkinter import ttk, messagebox
import math

class AreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")

        self.tabControl = ttk.Notebook(root)

        # Circle Tab
        self.circle_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.circle_tab, text="Circle")
        self.create_circle_tab()

        # Square Tab
        self.square_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.square_tab, text="Square")
        self.create_square_tab()

        # Rectangle Tab
        self.rectangle_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.rectangle_tab, text="Rectangle")
        self.create_rectangle_tab()

        self.tabControl.pack(expand=1, fill="both")

    def create_circle_tab(self):
        tk.Label(self.circle_tab, text="Radius:").grid(row=0, column=0, padx=10, pady=10)
        self.circle_radius_entry = tk.Entry(self.circle_tab)
        self.circle_radius_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.circle_tab, text="Calculate Area", command=self.calculate_circle_area)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_circle_area(self):
        try:
            radius = float(self.circle_radius_entry.get())
            if radius < 0:
                raise ValueError("Radius cannot be negative.")
            area = math.pi * radius**2
            messagebox.showinfo("Result", f"The area of the circle is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_square_tab(self):
        tk.Label(self.square_tab, text="Side Length:").grid(row=0, column=0, padx=10, pady=10)
        self.square_side_entry = tk.Entry(self.square_tab)
        self.square_side_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.square_tab, text="Calculate Area", command=self.calculate_square_area)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_square_area(self):
        try:
            side_length = float(self.square_side_entry.get())
            if side_length < 0:
                raise ValueError("Side length cannot be negative.")
            area = side_length**2
            messagebox.showinfo("Result", f"The area of the square is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_rectangle_tab(self):
        tk.Label(self.rectangle_tab, text="Length:").grid(row=0, column=0, padx=10, pady=10)
        self.rectangle_length_entry = tk.Entry(self.rectangle_tab)
        self.rectangle_length_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.rectangle_tab, text="Width:").grid(row=1, column=0, padx=10, pady=10)
        self.rectangle_width_entry = tk.Entry(self.rectangle_tab)
        self.rectangle_width_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.rectangle_tab, text="Calculate Area", command=self.calculate_rectangle_area)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_rectangle_area(self):
        try:
            length = float(self.rectangle_length_entry.get())
            width = float(self.rectangle_width_entry.get())
            if length < 0 or width < 0:
                raise ValueError("Length and width cannot be negative.")
            area = length * width
            messagebox.showinfo("Result", f"The area of the rectangle is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculator(root)
    root.mainloop() -->


&nbsp;
&nbsp;

------------------------------------------------------------------------------------------------------------------------------------------

## Exercise 4: Draw Shape☑️
Using tkinter module develop Gui to ask the user to select shapes like oval, rectangle, square, and triangle and draw the shape using canvas.

<!-- import tkinter as tk
from tkinter import ttk
import math

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.shape_var = tk.StringVar()
        self.shape_var.set("Select Shape")

        shape_options = ["Select Shape", "Oval", "Rectangle", "Square", "Triangle"]
        shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var, values=shape_options)
        shape_dropdown.pack(pady=10)

        draw_button = tk.Button(root, text="Draw", command=self.draw_shape)
        draw_button.pack(pady=10)

    def draw_shape(self):
        selected_shape = self.shape_var.get()

        if selected_shape == "Oval":
            self.draw_oval()
        elif selected_shape == "Rectangle":
            self.draw_rectangle()
        elif selected_shape == "Square":
            self.draw_square()
        elif selected_shape == "Triangle":
            self.draw_triangle()

    def draw_oval(self):
        self.canvas.create_oval(50, 50, 200, 150, fill="blue")

    def draw_rectangle(self):
        self.canvas.create_rectangle(50, 50, 200, 150, fill="green")

    def draw_square(self):
        self.canvas.create_rectangle(50, 50, 150, 150, fill="red")

    def draw_triangle(self):
        # Draw a simple equilateral triangle
        side_length = 100
        height = math.sqrt(3) / 2 * side_length

        x1, y1 = 150, 50
        x2, y2 = x1 + side_length, y1
        x3, y3 = x1 + side_length / 2, y1 + height

        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="purple")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root)
    root.mainloop() -->

&nbsp;
### Extension 
Ask the user to input the coordinate values of the selected option

<!-- import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.shape_var = tk.StringVar()
        self.shape_var.set("Select Shape")

        shape_options = ["Select Shape", "Oval", "Rectangle", "Square", "Triangle"]
        shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var, values=shape_options)
        shape_dropdown.pack(pady=10)

        self.coordinate_label = tk.Label(root, text="Enter Coordinates:")
        self.coordinate_label.pack()

        self.coordinate_entry = tk.Entry(root)
        self.coordinate_entry.pack(pady=5)

        draw_button = tk.Button(root, text="Draw", command=self.draw_shape)
        draw_button.pack(pady=10)

    def draw_shape(self):
        selected_shape = self.shape_var.get()
        coordinates = self.coordinate_entry.get()

        if selected_shape == "Select Shape":
            tk.messagebox.showwarning("Warning", "Please select a valid shape.")
            return

        try:
            coordinates = list(map(int, coordinates.split(',')))

            if selected_shape == "Oval":
                self.draw_oval(coordinates)
            elif selected_shape == "Rectangle":
                self.draw_rectangle(coordinates)
            elif selected_shape == "Square":
                self.draw_square(coordinates)
            elif selected_shape == "Triangle":
                self.draw_triangle(coordinates)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid coordinates. Please enter valid integer values.")

    def draw_oval(self, coordinates):
        if len(coordinates) == 4:
            self.canvas.create_oval(coordinates, fill="blue")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Oval.")

    def draw_rectangle(self, coordinates):
        if len(coordinates) == 4:
            self.canvas.create_rectangle(coordinates, fill="green")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Rectangle.")

    def draw_square(self, coordinates):
        if len(coordinates) == 4:
            self.canvas.create_rectangle(coordinates, fill="red")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Square.")

    def draw_triangle(self, coordinates):
        if len(coordinates) == 6:
            self.canvas.create_polygon(coordinates, fill="purple")
        else:
            tk.messagebox.showerror("Error", "Invalid number of coordinates for Triangle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root)
    root.mainloop() -->

&nbsp;
&nbsp;

#------------------------------------------------------Bonus Exercises--------------------------------------------------------------------

## Bonus Assessment Exercise - Burger Shack Vendor

Burger Shack is about to open in RAK, however, the fast food chain is in need of an ordering system. Write a program to handle the ordering process for the burger shack. The program should include:

* The ability to choose between at least three burger types (e.g. Beef, Chicken, Vegetarian)
* The ability to add toppings, with at least three to choose from (e.g. cheese, peanut butter, avocado)
* The ability to add condiments, with at least three to choose from (e.g. ketchup, mayonnaise, bbq sauce)
* The ability to add sides, these can include items such as fries and drinks.
* The ability to handle payment and return change to the user


class BurgerShackOrder:
    def __init__(self):
        self.burger_types = ["Beef", "Chicken", "Vegetarian"]
        self.toppings = ["Cheese", "Peanut Butter", "Avocado"]
        self.condiments = ["Ketchup", "Mayonnaise", "BBQ Sauce"]
        self.sides = ["Fries", "Drink"]
        self.order = {"burger_type": None, "toppings": [], "condiments": [], "sides": []}

    def display_menu(self):
        print("Welcome to Burger Shack!")
        print("\nMenu:")
        print("1. Burger Types:")
        for i, burger_type in enumerate(self.burger_types, start=1):
            print(f"   {i}. {burger_type}")
        print("\n2. Toppings:")
        for i, topping in enumerate(self.toppings, start=1):
            print(f"   {i}. {topping}")
        print("\n3. Condiments:")
        for i, condiment in enumerate(self.condiments, start=1):
            print(f"   {i}. {condiment}")
        print("\n4. Sides:")
        for i, side in enumerate(self.sides, start=1):
            print(f"   {i}. {side}")

    def take_order(self):
        self.display_menu()

        # Choose burger type
        burger_choice = int(input("\nEnter the number of the burger type: "))
        self.order["burger_type"] = self.burger_types[burger_choice - 1]

        # Add toppings
        print("\nChoose toppings (separate numbers by commas, or enter 0 for none):")
        topping_choices = input().split(',')
        for choice in topping_choices:
            if choice != '0':
                self.order["toppings"].append(self.toppings[int(choice) - 1])

        # Add condiments
        print("\nChoose condiments (separate numbers by commas, or enter 0 for none):")
        condiment_choices = input().split(',')
        for choice in condiment_choices:
            if choice != '0':
                self.order["condiments"].append(self.condiments[int(choice) - 1])

        # Add sides
        print("\nChoose sides (separate numbers by commas, or enter 0 for none):")
        side_choices = input().split(',')
        for choice in side_choices:
            if choice != '0':
                self.order["sides"].append(self.sides[int(choice) - 1])

    def calculate_total(self):
        # Assuming a simple pricing scheme
        burger_price = 5.0  # Price for each burger
        topping_price = 1.0  # Price for each topping
        condiment_price = 0.5  # Price for each condiment
        side_price = 2.0  # Price for each side

        total_price = burger_price + len(self.order["toppings"]) * topping_price + \
                      len(self.order["condiments"]) * condiment_price + \
                      len(self.order["sides"]) * side_price

        return total_price

    def process_payment(self, amount_paid):
        total_price = self.calculate_total()
        change = amount_paid - total_price
        return change

    def print_receipt(self):
        print("\nYour Order:")
        print(f"Burger Type: {self.order['burger_type']}")
        print("Toppings:", ", ".join(self.order["toppings"]))
        print("Condiments:", ", ".join(self.order["condiments"]))
        print("Sides:", ", ".join(self.order["sides"]))
        print(f"\nTotal Price: ${self.calculate_total():.2f}")

# Example Usage
order = BurgerShackOrder()
order.take_order()

amount_paid = float(input("\nEnter the amount paid: $"))
change = order.process_payment(amount_paid)

print("\nThank you for ordering from Burger Shack!")
order.print_receipt()
print(f"\nChange: ${change:.2f}")

You should design your program to make use of functions and pass information to and from these as appropriate. Alongside the above requirements, you are free to extend the functionality of the program as you see fit.



&nbsp;
&nbsp;

------------------------------------------------------------------------------------------------------------------------------------------

# Further Exercise
## Exercise I: Vending Machine
#Redo the vending machine app developed by you in Codelab-I using the tkinter module


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

&nbsp;
&nbsp;

#-----------------------------------------------------------------------------------------------------------------------------------------

# Exercise II: Guess Word
#Develop an interactive app using the tkinter module to guess the word, the app should show some random shuffle words and ask user to #guess the words, you can count the score for each correct answer and display the final score. You are free to extend requirements like #providing the timer, different levels etc.

import tkinter as tk
import random
from tkinter import messagebox

class WordGuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")

        self.words = ["python", "java", "html", "css", "javascript", "django", "react", "angular", "flask", "sql"]
        self.level = tk.StringVar()
        self.level.set("easy")
        self.score = 0
        self.time_limit = 30
        self.current_timer = None

        self.create_widgets()

    def create_widgets(self):
        # Level selection
        level_label = tk.Label(self.root, text="Select Level:")
        level_label.grid(row=0, column=0, padx=10, pady=10)

        level_dropdown = tk.OptionMenu(self.root, self.level, "easy", "medium", "hard")
        level_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Score display
        score_label = tk.Label(self.root, text="Score:")
        score_label.grid(row=0, column=2, padx=10, pady=10)

        self.score_display = tk.Label(self.root, text="0")
        self.score_display.grid(row=0, column=3, padx=10, pady=10)

        # Word display
        self.word_display = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.word_display.grid(row=1, column=0, columnspan=4, pady=20)

        # Entry for user input
        self.user_input = tk.Entry(self.root, font=("Helvetica", 14))
        self.user_input.grid(row=2, column=0, columnspan=4, pady=10)
        self.user_input.bind("<Return>", self.check_guess)

        # Start button
        start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        start_button.grid(row=3, column=0, columnspan=4, pady=10)

    def start_game(self):
        self.score = 0
        self.score_display.config(text="0")
        self.start_round()

    def start_round(self):
        self.user_input.delete(0, tk.END)
        self.current_word = random.choice(self.words)
        shuffled_word = ''.join(random.sample(self.current_word, len(self.current_word)))
        self.word_display.config(text=shuffled_word)
        self.start_timer()

    def start_timer(self):
        self.time_remaining = self.time_limit
        self.update_timer_display()
        self.current_timer = self.root.after(1000, self.update_timer)

    def update_timer(self):
        self.time_remaining -= 1
        self.update_timer_display()

        if self.time_remaining > 0:
            self.current_timer = self.root.after(1000, self.update_timer)
        else:
            self.root.after_cancel(self.current_timer)
            self.end_round()

    def update_timer_display(self):
        self.word_display.config(text=f"Time: {self.time_remaining}s | {self.current_word}")

    def check_guess(self, event):
        user_guess = self.user_input.get()

        if user_guess == self.current_word:
            self.score += 1
            self.score_display.config(text=str(self.score))
            self.start_round()
        else:
            messagebox.showinfo("Incorrect", "Try again!")

    def end_round(self):
        messagebox.showinfo("Time's Up", f"Your score: {self.score}")
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessGame(root)
    root.mainloop()


----------------------------------------------------END OF THE CHAPTER----------------------------------------------------------------=