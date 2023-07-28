# LeetCode 146
# less recent ------> more recent

class Node:
        
    def __init__(self, key, value):
        
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.space = capacity
        self.cache = {}
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.previous = self.tail
        self.tail.next = self.head

    def get(self, key: int) -> int:

        try:
            node = self.cache[key]
            self.insert(node)
            return node.value
        except KeyError:
            return -1 

    def insert(self, node):

        node.previous.next, node.next.previous = node.next, node.previous
     
        original_second = self.head.previous
        original_second.next = node
      
        node.previous = original_second
        node.next = self.head
       
        self.head.previous = node
        
    def put(self, key: int, value: int) -> None:
        
        try:
            node = self.cache[key]
            node.value = value
            self.insert(node)
        except KeyError:
            
            if not self.space:
                oldest = self.tail.next 
                self.cache.pop(oldest.key)
                self.tail.next = oldest.next
                oldest.next.previous = self.tail
                self.space += 1

            
            node = Node(key, value)
            self.cache[key] = node
            node.next = self.head
            node.previous = self.head.previous
            node.previous.next = node
            self.head.previous = node
            self.space -= 1

        
    def print_cache(self):

        node = self.tail
        
        while node:
            print(f"[{node.key}]={node.value}  -> ", end="")
            node = node.next
        print("")

test_cache = LRUCache(2)
test_cache.print_cache()
test_cache.put(2, 2)
test_cache.print_cache()
test_cache.put(2, 1)
test_cache.print_cache()
test_cache.get(2)
test_cache.print_cache()