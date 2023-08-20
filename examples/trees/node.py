
class Node:
    
    def __init__(self, val, left=None, right=None):
        """Instantiates a node."""
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node (value: {str(self.val)})"


