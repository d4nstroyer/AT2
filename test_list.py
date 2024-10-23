# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5 12:49:14 2024

@author: Danny - 20115804
Version 1.0
NM TAFE
"""

import unittest
from listfunction import add_to_list, sort_list, delete_from_list, search_in_list

# Test Cases
class TestLists(unittest.TestCase):

    def test_add_to_list(self): 
        test_list = []
        result = add_to_list(test_list, "Danny") 
# if correct: 
        self.assertEqual(result, ["Danny"]) 
# check if its successful
        self.assertEqual(test_list, ["Danny"]) 

    def test_sort_list(self): 
        test_list = ["Rafli", "Nadifa", "Danny"] 
        result = sort_list(test_list) 
# if its correct: 
        self.assertEqual(result, ["Danny", "Nadifa", "Rafli"]) 

    def test_delete_from_list(self): 
        test_list = ["Danny", "Nadifa", "Rafli"] 
        result = delete_from_list(test_list, "Rafli") 
# if its correct: 
        self.assertEqual(result, ["Danny", "Nadifa"]) #list will change to this, as alan has been deleted

    def test_delete_failed(self): 
        test_list = ["Danny", "Nadifa", "Rafli"] 
        delete_from_list(test_list, "Hong")
# check if the list remain unchanged
        self.assertEqual(test_list, ["Danny", "Nadifa", "Rafli"])
        
    def test_search_in_list(self):
        test_list = ["Danny", "Nadifa", "Rafli"]
        result = search_in_list(test_list, "Danny")
        self.assertEqual(result, ["Danny", "Nadifa", "Rafli"])

if __name__ == '__main__':
    unittest.main()
