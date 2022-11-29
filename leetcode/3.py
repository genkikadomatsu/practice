def lc3(s: str) -> int:

    if len(s) == 0:
        return 0
    

    maxlen = 1 # maximum length
    a, b = 0, 0 # pointers
    seen = {}

    while b < len(s):

        if s[b] in seen:
            if a <= seen[s[b]]:
                a = seen[s[b]] + 1
                
        maxlen = max(maxlen, b - a + 1)
        seen[s[b]] = b
        b += 1

    return maxlen


t1 = "t" # 1
t2 = "tm" # 2
t3 = "tmm" # 2
t4 = "tmmz" # 2
t5 = "tmmzu" # 3
t6 = "tmmzux" # 4
t7 = "tmmzuxt" # 5
