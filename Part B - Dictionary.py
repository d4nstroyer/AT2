# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5 14:38:25 2024

@author: Danny - 20115804
Version 1.0
NM TAFE

- A list that stores at least 12 of your favourite actors/actresses’ names.
- A list that stores at least 12 of your favourite movies and release year.
- A list that stores at least 12 of your favourite games and release year.

1.1.	Create a dictionary from the scenario above
1.2.	Add a value to the dictionary
1.3.	Delete a value from the dictionary
1.4.	Sort all the data in the dictionary in the ascending order. Sort all the data in the dictionary in the descending order. 
1.5.	Search for the value in the dictionary asking user for input.
"""

# Create dictionaries for actors with their birthdays, movies with their release years, and games with their release years
actor_dict = {
    "Robert Downey Jr.": "April 4, 1965", 
    "Chris Evans": "June 13, 1981", 
    "Scarlett Johansson": "November 22, 1984", 
    "Mark Ruffalo": "November 22, 1967",
    "Chris Hemsworth": "August 11, 1983", 
    "Tom Holland": "June 1, 1996", 
    "Samuel L. Jackson": "December 21, 1948", 
    "Jeremy Renner": "January 7, 1971",
    "Paul Rudd": "April 6, 1969", 
    "Elizabeth Olsen": "February 16, 1989", 
    "Benedict Cumberbatch": "July 19, 1976", 
    "Brie Larson": "October 1, 1989"
}

movie_dict = {
    "Iron Man": 2008, 
    "The Avengers": 2012, 
    "Captain America": 2011,
    "Thor": 2011, 
    "Spider-Man: Homecoming": 2017, 
    "Doctor Strange": 2016,
    "Black Panther": 2018, 
    "Ant-Man": 2015, 
    "Guardians of the Galaxy": 2014,
    "Avengers: Endgame": 2019, 
    "Avengers: Infinity War": 2018, 
    "Captain Marvel": 2019
}

game_dict = {
    "Dark Souls III": 2016, 
    "Elden Ring": 2022, 
    "Lies of P": 2023,
    "Borderlands 2": 2012, 
    "Borderlands 3": 2019, 
    "DotA": 2013, 
    "CS:GO": 2012, 
    "The Witcher 3": 2015, 
    "Cyberpunk 2077": 2020, 
    "Hades": 2020, 
    "Sekiro: Shadows Die Twice": 2019, 
    "Hollow Knight": 2017
}

# Function for dictionary operations
def add_to_dict(category_dict, key, value):
    category_dict[key] = value
    return category_dict

def delete_from_dict(category_dict, key):
    if key in category_dict:
        del category_dict[key]
    else:
        print(f"{key} not found in the dictionary.")  
    return category_dict

# Function to sort a dictionary by its keys in place
def sort_value(category_dict):
    sorted_keys = sorted(category_dict.keys())  # Sorts the keys
    return {key: category_dict[key] for key in sorted_keys}  # Returns a new sorted dictionary

def search_in_dict(category_dict, key):
    if key in category_dict:
        print(f"{key}: {category_dict[key]} is found in the dictionary.")
    else:
        print(f"{key} not found in the dictionary.")
    return category_dict

# Main loop to interact with the user
while True: 
    # Prompt user for category type
    category_type = input("Please enter category type: A(ctor), M(ovie), G(ames), E(nd) => ").strip().upper()
    
    if category_type == 'E':
        print("Exiting the program.")
        break
    else:
        if category_type == 'A':
            category_dict = actor_dict
        elif category_type == 'M':
            category_dict = movie_dict
        elif category_type == 'G':
            category_dict = game_dict
        else:
            print("Unknown input:", category_type)
            continue
            
        # Nested loop for specific instructions on the selected category
        while True:
            instruction_type = input("Please enter instruction: A(dd), D(elete), S(orting), sea(R)ch, P(revious menu) => ").strip().upper()
            if instruction_type == 'P':
                break
            elif instruction_type == 'A':
                if category_type == 'M' or category_type == 'G':
                    name = input("Enter the name: ")
                    year = int(input("Enter the release year: "))
                    category_dict = add_to_dict(category_dict, name, year) 
                else:
                    name = input("Enter an actor's name: ")
                    birthday = input("Enter the actor's birthday: ")
                    category_dict = add_to_dict(category_dict, name, birthday) 
            elif instruction_type == 'D':
                name = input("Enter a name to delete: ")
                category_dict = delete_from_dict(category_dict, name) 
            elif instruction_type == 'S':
                sorted_dict = sort_value(category_dict)  # Use sort_value function to sort
                print("Sorted Dictionary:")
                for key, value in sorted_dict.items():
                    print(f"{key}: {value}")
            elif instruction_type == 'R':
                name = input("Enter a name to search: ")
                category_dict = search_in_dict(category_dict, name)  
            else:
                print("Invalid instruction. Please try again.")  


