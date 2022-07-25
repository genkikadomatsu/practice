class MyQueue:

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

        
    def maintain_FIFO(self):
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
                
    def push(self, x: int) -> None:
        self.stack_a.append(x)

    def pop(self) -> int:
        self.maintain_FIFO()
        return self.stack_b.pop()

    
    def peek(self) -> int:
        self.maintain_FIFO()
        return self.stack_b[-1]

    # if both stacks are empty, we have an empty queue
    def empty(self) -> bool:
        return (not self.stack_a) and (not self.stack_b)