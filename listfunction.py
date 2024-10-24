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

# Functions for list operations
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

def play():
    while True:
        category_type = input("Please Enter category type e.g., A(ctors), M(ovies), G(ames), E(nd) => ").strip().upper()

        if category_type == 'E':
            print("Thank you. You are now exiting the program.")
            break
        
        if category_type == 'A':
            list_type = actor_list
        elif category_type == 'M':
            list_type = movie_list
        elif category_type == 'G':
            list_type = game_list
        else:
            print("Unknown input:", category_type)
            continue

        while True:
            instruction_type = input("Please enter instruction type e.g., A(dd), D(elete), S(orting), sea(R)ch, P(revious menu) => ").strip().upper()

            if instruction_type == "P":
                break
            elif instruction_type == "A":
                value = input("Please Enter Value: ")
                list_type = add_to_list(list_type, value)
            elif instruction_type == "D":
                value = input("Please Enter Value: ")
                list_type = delete_from_list(list_type, value)
            elif instruction_type == "S":
                list_type = sort_list(list_type)
            elif instruction_type == "R":
                value = input("Please enter value to search: ")
                search_in_list(list_type, value)
            else:
                print("Invalid instruction")
                continue

            print(list_type)

if __name__ == '__main__':
    play()


