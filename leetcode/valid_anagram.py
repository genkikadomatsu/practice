class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        
        for c in t:
            if c in d:
                d[c] = d[c] - 1
                if d[c] < 0:
                    return False
            else:
                return False
        return True

sol = Solution()
sol.isAnagram("bo", "bob") #false

