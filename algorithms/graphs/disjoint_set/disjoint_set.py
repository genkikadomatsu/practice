"""
disjoint_set.py

For demonstration purposes, this is intentionally without path compression.

Wiki on disjoint sets: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""
from collections.abc import Iterable
from typing import Any

class DisjointSet:
    """Disjoint-set data structure (aka Union find).
    
    The disjoint set is a data structure that stores non-overlapping groups of
    elements (of arbitrary type). Each group has a 'representative' element,
    which represents the group. We can think of this representative element as
    the parent of the group.

    We have two operations on a disjoint-set:
        Union: Combines two non-overlapping groups.
        Find: Returns the representative element of the group. 
    """

    def __init__(self, set: Iterable):
        """
        Initializes the disjoint set given a set of elements.

        :param set: The input set of elements (of arbitrary type). 
        """
        
        self.elem_list = list(set)
        self.group_id_list = [n for n in range(len(self.elem_list))]
    
    def union(self, parent_elem: Any, child_elem: Any) -> None:
        """
        Combines the groups of two elements.
        """

        parent_elem_id = self.group_id_list[self.elem_list.index(parent_elem)]
        child_elem_id = self.elem_list.index(child_elem)
        self.group_id_list[child_elem_id] = parent_elem_id

    def find(self, elem: Any) -> Any:
        """
        Returns the representative element of the group of a given element.

        :param elem: The element whose group's representative element to return.
        :return: The representative element of the group of the input element.
        """

        elem_id = self.elem_list.index(elem)
        group_id = self.group_id_list[elem_id]

        while elem_id != group_id:
            elem = self.elem_list[group_id]
            elem_id = self.elem_list.index(elem)
            group_id = self.group_id_list[elem_id]

        return elem
