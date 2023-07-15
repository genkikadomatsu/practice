from typing import List
from collections import deque

class Node:

    def __init__(self, c: str | None):
        
        self.c = c
        self.map = {}
        self.ends_word = False

    def search(self, c: str) -> 'Node | None':
        """Return the node of the character in this Node's map if it exists."""
     
        if c not in self.map:
            return None
    
        return self.map[c]

    def insert(self, next_c: str):
        """Insert an outgiong Node to this Node's map if it doesn't exist yet.""" 

        if next_c not in self.map:
            self.map[next_c] = Node(next_c)

        return self.map[next_c]

class WordDictionary:

    WILDCARD = "."

    def __init__(self):
        self.root = Node(None)


    def addWord(self, word: str) -> None:
        
        current_node = self.root
        
        for c in word:
            print(f"Adding {c} to node {current_node.c}...")
            current_node = current_node.insert(c)

        current_node.ends_word = True


    def search(self, word: str) -> bool:

        def recurse(current_i, node):
            for i in range(current_i, len(word)):
                if word[i] == self.WILDCARD:
                    for potentially_next_node in node.map.values():
                        if recurse(i + 1, potentially_next_node):
                            return True
                    return False
                else:
                    if word[i] not in node.map:
                        return False
                    node = node.map[word[i]] 
            return node.ends_word
    
        return recurse(0, self.root)