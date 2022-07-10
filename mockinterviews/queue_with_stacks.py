class MyQueue:
    """LeetCode 232"""

    def __init__(self):
        self.__a = [] #enqueue to a
        self.__b = [] #dequeue from b

    def __transfer_a_to_b(self):
        """ Transfer values from __a to __b"""
        while len(self.__a) > 0:
            self.__b.append(self.__a.pop())
    # Queue
    def push(self, x: int) -> None:
        """Queue a value."""
        self.__a.append(x)

    def pop(self) -> int:
        """If __b is empty, transfer all values from __a to __b."""
        if len(self.__b) == 0:
            self.__transfer_a_to_b()
        return self.__b.pop()

    def peek(self) -> int:
        """Return the value in the front of the queue"""
        if len(self.__b) == 0:
            self.__transfer_a_to_b()
        return self.__b[-1]

    def empty(self) -> bool:
        """Determine if the queue is empty"""
        return not (len(self.__a) + len(self.__b))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()