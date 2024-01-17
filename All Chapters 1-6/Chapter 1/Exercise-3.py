# Write a program that asks the user to enter the lengths of the three sides of a triangle.
# Use the triangle inequality to determine if we have a triangle: In mathematics, the triangle inequality states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side

def is_triangle(side1, side2, side3):
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

# Prompt user for the lengths of the three sides
side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))

# Check if the sides form a triangle
if is_triangle(side1, side2, side3):
    print("These side lengths form a valid triangle.")
else:
    print("These side lengths do not form a valid triangle.")

# -----------------------Extention--------------------
    
# If valid, ask the user for the length of the sides and have the program correctly classify the type of triangle as either: Equilateral, Isosceles or Scalene
    
def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

def is_triangle(side1, side2, side3):
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

# Prompt user for the lengths of the three sides
side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))

# Check if the sides form a triangle
if is_triangle(side1, side2, side3):
    triangle_type = classify_triangle(side1, side2, side3)
    print(f"These side lengths form a valid {triangle_type} triangle.")
else:
    print("These side lengths do not form a valid triangle.")
