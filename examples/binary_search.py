"""binary_search.py

Python implementation of binary search.
"""
from typing import List

class BinarySearch:

    @staticmethod
    def binary_search_twopointer(input: List[int], target: int) -> bool:
        """Returns the index of the value which matches target.

        This is a 'two pointers' style implementation for binary search.

        :param input: A sorted (ascending) list of integers.
        :param target: The integer to search for.
        :return: The index of the target integer in the input list.
        :throws: Exception if the target is not in the list. 
        """
        
        lower_bound, upper_bound = 0, len(input) - 1

        while lower_bound <= upper_bound:
            # The stopping condition here has to be leq, because we need to have
            # one iteration where lower_bound and upper_bound are overlapping,
            # to account for this case: ([1,2,3], 3) or ([1,2,3], 1).
            
            i = (lower_bound + upper_bound) // 2
            v = input[i]

            if target > v:
                lower_bound = i + 1
            elif target < v:
                upper_bound = i - 1
            else:
                return i
        
        raise Exception(f"Value {target} isn't in {input}.")

assert 0 == BinarySearch.binary_search_twopointer([1,2,3], 1)
assert 1 == BinarySearch.binary_search_twopointer([1,2,3], 2)
assert 2 == BinarySearch.binary_search_twopointer([1,2,3], 3)
