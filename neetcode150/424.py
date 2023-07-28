# 242 LeetCode

def characterReplacement(s: str, k: int) -> int:

    result = 0
    
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        current_k_usage = 0
        start_index = 0

        for index in range(len(s)): 

            # Add to k-usage if we are now using another k
            if s[index] != letter:
                current_k_usage += 1

            # If we're past k-capacity, we need to shift the start pointer until we are good 
            while current_k_usage > k and start_index < index:
                if s[start_index] != letter:
                    current_k_usage -= 1
                start_index += 1

            # If we attempted to shift the start pointer to decrease k-usage, but it is still above capacity
            # - that means we shouldn't calculate the new max because it is an illegal k-usage ammount 
            # - this can only happen if start_index = index and current_k_usage is still more than k, which means
            #   - that this condition only happens when k == 0
            if current_k_usage > k:
                print("Special continue case")
                continue
            
            # If we successfully decreased k-usage, we can calculate the new length
            result = max(index - start_index + 1, result)
    
    return result


while True:
    print(characterReplacement(input("s:"), int(input("k:"))))