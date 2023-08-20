"""Interactive program that can be used to learn about tree traversals."""

from typing import Any
from binary_tree import BinaryTree
from node import Node
from collections.abc import Iterable
from collections import deque

TREE_ROOT = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
EXPRESSION_TREE_ROOT = Node('+', Node(3), Node('*', Node('+', Node(5), Node(9)), Node(2)))

class Traversals:

    @staticmethod
    def inorder(root: Node) -> Iterable:
        if root:
            yield from Traversals.inorder(root.left)
            yield root.val
            yield from Traversals.inorder(root.right)

    @staticmethod
    def preorder(root: Node) -> Iterable:
        if root:
            yield root.val
            yield from Traversals.preorder(root.left)
            yield from Traversals.preorder(root.right)

    @staticmethod
    def postorder(root: Node) -> Iterable:
        if root:
            yield from Traversals.postorder(root.left)
            yield from Traversals.postorder(root.right)
            yield root.val

    @staticmethod
    def levelorder(root: Node) -> Iterable:
        
        if not root:
            yield root.val

        queue = deque([root])
        
        while queue:
            level = []

            for i in range(len(queue)):
            # This works here because the for loop evaluates the size of the queue
            # only once at the start of the iterations.
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
            
                if node.right:
                    queue.append(node.right)

            yield level    
        

def handle_input(input: str) -> bool:

    if input == "q":
        return False

    if not (
        input in dir(Traversals) 
        and callable((getattr(Traversals, input)))
    ):
        print("That traversal method is not implemented yet, fuck off please!")
        return True

    for x in getattr(Traversals, input)(TREE_ROOT):
        print(x, end=" ")

    print("")
    
    return True


if __name__ == "__main__":

    traversals = [t for t in dir(Traversals) if t[:2] != "__"]
    print("Enter a traversal:") 
    
    for t in traversals:
        print(" -", t)
    
    while handle_input(input("or 'q' to quit: ")):
        print("- " * 40) 
        print("Enter a traversal:") 
        for t in traversals:
            print(" -", t)
    