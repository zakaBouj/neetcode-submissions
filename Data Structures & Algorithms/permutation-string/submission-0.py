class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = "".join(sorted(s1))
        left = 0
        right = len(s1) - 1
   
        while right < len(s2):
            sub_str_sorted = "".join(sorted(s2[left:right + 1]))
            if sub_str_sorted == s1_sorted:
                return True         
            left += 1
            right += 1

        return False