# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:05:50 2024

@author: Danny - 20115804
Version 1.0
NM TAFE
"""

import unittest
from dictionaryfunction import add_to_dict, delete_from_dict, sort_dict, search_in_dict

class TestDictFunctions(unittest.TestCase):
    def add_to_dict(self):
        test_dict = {}
        add_to_dict(test_dict, "David Beckham", 1975) 
        self.assertEqual(add_to_dict, {"David Beckham": 1975})  

    def delete_from_dict(self): 
        test_dict = {"David Beckham": 1975, "Christiano Ronaldo": 1985, "Lionel Messi": 1987} 
        result = delete_from_dict(test_dict, "David Beckham") #David Beckham will be deleted
#if its successful: 
        self.assertEqual(result, {"Christiano Ronaldo": 1985, "Lionel Messi": 1987} ) #David Beckham should be removed

    def test_delete_not_found(self):
        test_dict = {"Christiano Ronaldo": 1985, "Lionel Messi": 1987} #David Beckham is not in dictionary
        result = delete_from_dict(test_dict, "David Beckham")  # Attempt to delete a non-existent entry 
        self.assertEqual(result, {"Christiano Ronaldo": 1985, "Lionel Messi": 1987})  # Verify that the dictionary remains unchanged

    def test_sort_dict(self):
        test_dict = {"David Beckham": 1975, "Christiano Ronaldo": 1985, "Lionel Messi": 1987} #dictionary is not sorted
        result = sort_dict(test_dict)
        expected_result = {"Christiano Ronaldo": 1985, "David Beckham": 1975, "Lionel Messi": 1987 } #to compare directly with the dictionary output, avoiding tuple-based comparisons.
        self.assertEqual(result, expected_result)  #sorted in ascending order
   
    def test_search_in_dict_found(self):
        test_dict = {"David Beckham": 1975, "Christiano Ronaldo": 1985} #David Beckham is in the dictionary
        result = search_in_dict(test_dict, "David Beckham") #input David Beckham
        self.assertEqual(result, {'David Beckham': 1975, 'Christiano Ronaldo': 1985}) #David Beckham appears on the result
        
    def test_search_in_dict_not_found(self):
        test_dict = {"David Beckham": 1975, "Christiano Ronaldo": 1985} #Lionel Messi is not in dictionary
        result = search_in_dict(test_dict, "Lionel Messi") #input Lionel Messi
        self.assertEqual(result, {"David Beckham": 1975, "Christiano Ronaldo": 1985}) #Lionel Messi will not appear on the result

if __name__ == '__main__':
    unittest.main()