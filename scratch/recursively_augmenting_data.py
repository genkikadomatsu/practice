# Recursive data does not "return" back to it's previous state when returning from recursion.
def example(l, i):
    
    print(l, i)
    if len(l) > 5 or i > 5:
        return

    example(l, i + 1)

    l.append(1)
    example(l, i + 1)

    #implicit return at the end of the function (returning with augmented l)



a = []
b = 0

example(a, b)
    