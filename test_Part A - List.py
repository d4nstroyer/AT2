# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5 12:49:14 2024

@author: Danny - 20115804
Version 1.0
NM TAFE
"""

import unittest

# The main functions you want to test
def add_to_list(category_list, value):
    category_list.append(value)
    return category_list

def delete_from_list(category_list, value):
    if value in category_list:
        category_list.remove(value)
    return category_list

def sort_list(category_list, descending=False):
    return sorted(category_list, reverse=descending)

def search_in_list(category_list, value):
    return value in category_list

# Test Cases
class TestFavoriteLists(unittest.TestCase):

    def setUp(self):
        self.actors = ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson"]
        self.movies = [("Iron Man", 2008), ("The Avengers", 2012)]
        self.games = [("Dark Souls III", 2016), ("Elden Ring", 2022)]

    def test_add_to_list(self):
        # Test adding an actor
        add_to_list(self.actors, "Tom Holland")
        self.assertIn("Tom Holland", self.actors)

        # Test adding a movie
        add_to_list(self.movies, ("Spider-Man: Homecoming", 2017))
        self.assertIn(("Spider-Man: Homecoming", 2017), self.movies)

        # Test adding a game
        add_to_list(self.games, ("Hades", 2020))
        self.assertIn(("Hades", 2020), self.games)

    def test_delete_from_list(self):
        # Test deleting an actor
        delete_from_list(self.actors, "Chris Evans")
        self.assertNotIn("Chris Evans", self.actors)

        # Test deleting a movie
        delete_from_list(self.movies, ("The Avengers", 2012))
        self.assertNotIn(("The Avengers", 2012), self.movies)

        # Test deleting a game
        delete_from_list(self.games, ("Elden Ring", 2022))
        self.assertNotIn(("Elden Ring", 2022), self.games)

    def test_sort_list(self):
        # Test sorting actors in ascending order
        sorted_actors = sort_list(self.actors)
        self.assertEqual(sorted_actors, sorted(self.actors))

        # Test sorting movies in descending order
        sorted_movies_desc = sort_list(self.movies, descending=True)
        self.assertEqual(sorted_movies_desc, sorted(self.movies, reverse=True))

        # Test sorting games in ascending order
        sorted_games = sort_list(self.games)
        self.assertEqual(sorted_games, sorted(self.games))

    def test_search_in_list(self):
        # Test searching for an actor
        self.assertTrue(search_in_list(self.actors, "Robert Downey Jr."))
        self.assertFalse(search_in_list(self.actors, "Chris Pratt"))

        # Test searching for a movie
        self.assertTrue(search_in_list(self.movies, ("Iron Man", 2008)))
        self.assertFalse(search_in_list(self.movies, ("Avatar", 2009)))

        # Test searching for a game
        self.assertTrue(search_in_list(self.games, ("Dark Souls III", 2016)))
        self.assertFalse(search_in_list(self.games, ("Call of Duty", 2003)))

# Run the tests
if __name__ == '__main__':
    unittest.main()
