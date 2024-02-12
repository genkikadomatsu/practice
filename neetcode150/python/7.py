"""7"""
class Solution:
    def reverse(self, x: int) -> int:
        max_32int = 2147483647
        min_32int = -2147483648
        reversed = 0

        while x:
            print(x, reversed)
            new_digit = -(abs(x) % 10) if x < 0 else x % 10

            # Check upper bound
            if (reversed > (max_32int // 10)) or (reversed == max_32int // 10 and new_digit >= max_32int % 10):
                print("asdf", reversed, max_32int, x)
                return 0

            # Check lower bound
            if (reversed < (min_32int // 10)) or (reversed == min_32int // 10 and new_digit <= min_32int % 10):
                return 0

            reversed = (reversed * 10) + new_digit
            x = int(x / 10)

        return reversed
