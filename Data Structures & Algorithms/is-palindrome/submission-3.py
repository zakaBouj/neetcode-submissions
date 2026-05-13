class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = "".join(c.lower() for c in s if c.isascii() and c.isalnum())
        
        left_ptr = 0
        right_ptr = len(alnum_s) - 1

        while left_ptr < right_ptr:
            if alnum_s[left_ptr] != alnum_s[right_ptr]:
                return False
            
            left_ptr += 1
            right_ptr -= 1

        return True