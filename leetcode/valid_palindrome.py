def isPalindrome(s: str) -> bool:
    '''Determine if the string is a palindrome.'''
    
    front = 0
    back  = len(s) - 1
    
    def is_alphanumeric(c):
        '''Determine if the string is alphanumeric.'''
        
        return (
                ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9")
                )
        
    while front < back:
        while (not is_alphanumeric(s[front])) and (front < back):
            front += 1
        while (not is_alphanumeric(s[back])) and (front < back):
            back -= 1
        
        if s[front].lower() != s[back].lower():
            return False
        
        front += 1
        back -= 1
    
    return True


if isPalindrome("Bab"):
    print("good")
else: print("bad")

if isPalindrome("!@#!@#!@#!@#!@Bob"): print("good")
else: print("bad")

if isPalindrome("A man, a plan, a canal: Panama"): print("good")
else: print("bad")

if not isPalindrome("race a car"): print("good")
else: print("bad")
