class Solution:
    def letterCombinations(self, digits: str):
        
        results = []

        # dfs append results
        def dfs(s, remaining_digits):


            if len(s) == len(digits):
                results.append(s)
                return
            
            for letter in self.digit_to_letters(remaining_digits[0]):
                dfs(s + letter, remaining_digits[1:])

        
        if not digits:
            return results
        
        dfs("", digits)
        return results


    @staticmethod
    def digit_to_letters(digit):
        match digit:
            case "2":
                return ["a", "b", "c"]
            case "3":
                return ["d", "e", "f"]
            case "4":
                return ["g", "h", "i"]
            case "5":
                return ["j", "k", "l"]
            case "6":
                return ["m", "n", "o"]
            case "7":
                return ["p", "q", "r", "s"]
            case "8":
                return ["t", "u", "v"]
            case "9":
                return ["w", "x", "y", "z"]



# Test Inputs
# 2 -> ["a", "b", "c"]
# 23 -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

s = Solution()
print(s.letterCombinations("2"))
print(s.letterCombinations("22"))
print(s.letterCombinations("23"))