from typing import List


def encode(ss:List[str])->str:

    result = ""

    for s in ss:
        result += str(len(s)) + "." + s
    
    return result


def decode(s:str)->List[str]:
    
    result = []
    i = 0
    while i < len(s):
        j = i
        current_number_string = ""

        while s[j] != ".":
            current_number_string += s[j]
            j += 1 
        j += 1
        
        length = int(current_number_string)
        word = ""
        j += 1 

        while length:
            word += s[j]
            length -= 1 
            print("Current word:", word)
            j += 1

        result.append(word) 
        i = j

    return result
