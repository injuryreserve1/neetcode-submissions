import re
import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r"[^a-zA-Z0-9]", "", s)
        r = len(text) - 1
        l = 0

        while l < r:
            l_char = text[l]
            r_char = text[r]

            r -= 1
            l += 1
            print(l_char, r_char)
            if l_char.lower() != r_char.lower():
                return False

        return True