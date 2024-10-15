# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5 12:01:39 2024

@author: Danny - 20115804
Version 1.0
NM TAFE

- A list that stores at least 12 of your favourite actors/actresses’ names.
- A list that stores at least 12 of your favourite movies and release year.
- A list that stores at least 12 of your favourite games and release year.

1. Write a Python program that provides the ability to: 
1.1. Create lists from the scenario above
1.2. Add a value to the list
1.3. Delete a value from the list
1.4. Sort all the data in the list in ascending order. Sort all the data in the list in descending order. 
1.5. Search for the value in the list asking user for input.
"""

# Create lists for actors, movies, and games
actor_list = [
    "Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
    "Chris Hemsworth", "Tom Holland", "Samuel L. Jackson", "Jeremy Renner",
    "Paul Rudd", "Elizabeth Olsen", "Benedict Cumberbatch", "Brie Larson"
]

movie_list = [
    "Iron Man", "The Avengers", "Captain America",
    "Thor", "Spider-Man: Homecoming", "Doctor Strange",
    "Black Panther", "Ant-Man", "Guardians of the Galaxy",
    "Avengers: Endgame", "Avengers: Infinity War", "Captain Marvel"
]

game_list = [
    "Dark Souls III", "Elden Ring", "Lies of P",
    "Borderlands 2", "Borderlands 3", "DotA", 
    "CS:GO", "The Witcher 3", "Cyberpunk 2077", 
    "Hades", "Sekiro: Shadows Die Twice", "Hollow Knight"
]

# Function for list operations
def add_to_list(category_list, value):
    category_list.append(value)
    return category_list

def delete_from_list(category_list, value):
    if value in category_list:
        category_list.remove(value)
    else:
        print(f"{value} not found in the list.")  
    return category_list

def sort_list(category_list, descending=False):
    return sorted(category_list, reverse=descending)

def search_in_list(category_list, value):
    if value in category_list:
        print(f"{value} is found in the list.")
    else:
        print(f"{value} not found in the list.")
    return category_list

# Main loop to interact with the user
while True: 
    # Prompt user for category type
    category_type = input("Please enter category type: A(ctor), M(ovie), G(ames), E(nd) => ").strip().upper()
    
    if category_type == 'E':
        print("Exiting the program.")
        break
    else:
        if category_type == 'A':
            category_list = actor_list
        elif category_type == 'M':
            category_list = movie_list
        elif category_type == 'G':
            category_list = game_list
        else:
            print("Unknown input:", category_type)
            continue
            
        # Nested loop for specific instructions on the selected category
        while True:
            instruction_type = input("Please enter instruction: A(dd), D(elete), S(orting), sea(R)ch, P(revious menu) => ").strip().upper()
            if instruction_type == 'P':
                break
            elif instruction_type == 'A':
                if category_type == 'M':
                    name = input("Enter a movie name: ")
                    year = int(input("Enter the release year: "))
                    category_list = add_to_list(category_list, (name, year)) 
                elif category_type == 'G':
                    name = input("Enter a game name: ")
                    year = int(input("Enter the release year: "))
                    category_list = add_to_list(category_list, (name, year))  
                else:
                    name = input("Enter an actor's name: ")
                    category_list = add_to_list(category_list, name) 
            elif instruction_type == 'D':
                if category_type == 'M' or category_type == 'G':
                    name = input("Enter a movie or game name to delete: ")
                    category_list = delete_from_list(category_list, (name, year))
                else:
                    name = input("Enter an actor's name to delete: ")
                    category_list = delete_from_list(category_list, name) 
            elif instruction_type == 'S':
                order = input("Sort in ascending or descending order? (A/D): ").strip().upper()
                sorted_list = sort_list(category_list, descending=(order == 'D'))  
                print("Sorted List:")
                for item in sorted_list:
                    print(item) 
            elif instruction_type == 'R':
                name = input("Enter a name to search: ")
                category_list = search_in_list(category_list, name)  
            else:
                print("Invalid instruction. Please try again.")  


