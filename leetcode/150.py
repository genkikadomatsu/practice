# LeetCode 150 Evaluate RPN
from collections import deque

TOKENS = ["+", "*", "-", "/"]

def calc(a, b, op): 
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b

def evalRPN(tokens: str) -> int:
 
    val_stack = []
    tokens = deque(tokens)

    while tokens:
        
        t = tokens.popleft() 

        if t in TOKENS:
            op = t
            b = val_stack.pop()
            a = val_stack.pop()
            t = calc(a, b, op)

        val_stack.append(int(t))
        
        print(val_stack)

    return val_stack[0]

while True:
    print(evalRPN(input("list:").split()))

