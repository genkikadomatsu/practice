
def characterReplacement(s: str, k: int) -> int:

    counts = {}
    current_letter = s[0]
    result = current_k_usage = current_max_c = current_start = 0
    
    for i in range(len(s)):

        print(s[i])
        
        # increment the counter, as this letter is now in our window        
        c = counts.get(s[i], 0) + 1
        print("    ", c)
        counts[s[i]] = c
        print("    ", counts)
        # update the max count if this one is now higher 
        if c >= current_max_c:
            print("    ", "updating the max count,", s[i], "is now the target at", c) 
            current_letter = s[i]
            current_max_c = c

        current_k_usage = i - current_start + 1 - current_max_c
        print("    updating k usage to", current_k_usage)

        # if the letter puts us over k-usage, attempt to shorten the window
        while current_k_usage > k and i > current_start:
                print("    over k usage so attempting to shorten window to decrease usage") 
                 
                if s[current_start] != current_letter:
                    current_k_usage -= 1
                counts[s[current_start]]  = counts[s[current_start]] - 1
                current_start += 1
                current_k_usage -= 1
                
        print("     ", counts)
        # If current_k_usage is no longer past capacity, we can calculate the new potential result
        if current_k_usage <= k:
            result = max(result, i - current_start + 1) 
            print("    current k usage is now", current_k_usage, ", updating the result to", result)

    return result 

while True:
    print(characterReplacement(input("s:"), int(input("k:"))))