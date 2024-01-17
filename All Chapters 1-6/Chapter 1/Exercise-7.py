# Write a program that prints the even numbers from 1 to 100. 
# Hint - Use Continue Statement

for num in range(1, 101):
    if num % 2 != 0:
        continue  # Skip odd numbers
    print(num)
