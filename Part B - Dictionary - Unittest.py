# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:05:50 2024

@author: Danny - 20115804
Version 1.0
NM TAFE
"""

import unittest

# Sample dictionaries for testing
actor_dict = {
    "Robert Downey Jr.": "April 4, 1965", 
    "Chris Evans": "June 13, 1981", 
    "Scarlett Johansson": "November 22, 1984"
}

movie_dict = {
    "Iron Man": 2008, 
    "The Avengers": 2012
}

game_dict = {
    "Dark Souls III": 2016, 
    "Elden Ring": 2022
}

# Functions from your code
def add_to_dict(category_dict, key, value):
    category_dict[key] = value
    return category_dict

def delete_from_dict(category_dict, key):
    if key in category_dict:
        del category_dict[key]
    return category_dict

def sort_value(category_dict):
    sorted_keys = sorted(category_dict.keys())
    return {key: category_dict[key] for key in sorted_keys}

def search_in_dict(category_dict, key):
    if key in category_dict:
        return category_dict[key]
    return None

class TestFavoriteMedia(unittest.TestCase):

    def test_add_to_dict(self):
        updated_dict = add_to_dict(actor_dict, "Mark Ruffalo", "November 22, 1967")
        self.assertIn("Mark Ruffalo", updated_dict)
        self.assertEqual(updated_dict["Mark Ruffalo"], "November 22, 1967")

    def test_delete_from_dict(self):
        updated_dict = delete_from_dict(actor_dict, "Chris Evans")
        self.assertNotIn("Chris Evans", updated_dict)

    def test_sort_value(self):
        sorted_dict = sort_value(movie_dict)
        expected_keys = sorted(movie_dict.keys())
        self.assertEqual(list(sorted_dict.keys()), expected_keys)

    def test_search_in_dict_found(self):
        value = search_in_dict(actor_dict, "Scarlett Johansson")
        self.assertEqual(value, "November 22, 1984")

    def test_search_in_dict_not_found(self):
        value = search_in_dict(actor_dict, "Unknown Actor")
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()

