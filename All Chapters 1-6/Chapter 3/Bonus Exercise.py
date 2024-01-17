# Burger Shack is about to open in RAK, however, the fast food chain is in need of an ordering system. Write a program to handle the ordering process for the burger shack. The program should include:

# * The ability to choose between at least three burger types (e.g. Beef, Chicken, Vegetarian)
# * The ability to add toppings, with at least three to choose from (e.g. cheese, peanut butter, avocado)
# * The ability to add condiments, with at least three to choose from (e.g. ketchup, mayonnaise, bbq sauce)
# * The ability to add sides, these can include items such as fries and drinks.
# * The ability to handle payment and return change to the user

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