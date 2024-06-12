import unittest
from sort_and_search import linear_search
from sort_and_search import insertion_sort
from sort_and_search import binary_search


class TestSortAndSearch(unittest.TestCase):
    # This function iterates through the list one item at a time until 
    # it finds the target element or reaches the end of the list.
    def test_linear_search(self):
        #Arrange:
        my_array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16]
        #Act:
        # Two arguments are expected: the array of numbers 
        # and the number we're searching for.
        result = linear_search(my_array, 5)
        #Assert:
        # The function is expected to return the index of 
        # the number 5, so the expected result is 3.
        self.assertEqual(result, 3)


    def test_insertion_sort(self):
        # This function iterates over the elements of the array
        # starting from index 1. For each element, it compares it with the elements
        # to its left, moving them one position to the right until it finds the
        # correct position to insert the current element.        
        #Arrange:
        my_array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 16, 100]
        expected_result = [-40, -3, 1, 2, 4, 5, 7, 16, 27, 35, 100]
        #Act:
        # The function takes an array of numbers as an argument.
        insertion_sort(my_array)
        #Assert:
        # We expect getting back the sorted array.
        self.assertEqual(my_array, expected_result)
        

    def test_binary_search(self):
        # This function repeatedly divides the portion of the list
        # that could contain the item in half, until it narrows down  
        # the possible locations to just one.
        #Arrange:
        my_array = [-40, -3, -1, 1, 4, 7, 9, 16, 18, 35, 100]
        #Act:
        # Pass the array and the number we search for as an argument.
        result = binary_search(my_array, 16)
        #Assert:
        # The function is expected to return the index of 
        # the number 16, so the expected result is 7.
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()

    