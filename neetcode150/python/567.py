def checkInclusion(s1: str, s2: str) -> bool:
    
    s1_count = {}
    for c in s1:
        s1_count[c] = s1_count.get(c, 0) + 1
    
    i = 0
    s1_len = len(s1)
    s2_subcount = {}

    for j in range(len(s2)):
        
        # Increment count of new i letter
        if j - i + 1 > s1_len:
            new_subcount = s2_subcount[s2[i]] = s2_subcount[s2[i]] - 1
            print(f"decrementing {s2[i]} to {new_subcount}")
            if new_subcount == 0:
                print(f"    popping because it is at 0")
                s2_subcount.pop(s2[i])
            i += 1


        # Increment count of j letter
        s2_subcount[s2[j]] = s2_subcount.get(s2[j], 0) + 1

        print(f"Iteration: {j}")
        print(f"s1_count: {s1_count}")
        print(f"s2_subcount: {s2_subcount}")
        print("")
        # If they have the same count, we've found a permutation
        if s2_subcount == s1_count:
            return True
    
    return False

while True:
    print(checkInclusion(input("s1:"), input("s2:")))
 