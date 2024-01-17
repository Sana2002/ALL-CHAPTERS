# Create a dictionary that contains relevant data for films (e.g. Title, Director, etc). Display the film details using loop

# Create a dictionary for a film
film_details = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Sci-Fi",
    "Rating": 8.8
}

# Display film details using a loop
print("Film Details:")
for key, value in film_details.items():
    print(f"{key}: {value}")
