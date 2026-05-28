class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        sub_str_freq = Counter(s2[0 : len(s1)])
        
        if sub_str_freq == s1_freq:
            return True

        left, right = 1, len(s1)
        while right < len(s2):        
            sub_str_freq[s2[right]] += 1
            sub_str_freq[s2[left - 1]] -= 1
            if sub_str_freq[s2[left - 1]] == 0:
                del sub_str_freq[s2[left - 1]]
            if sub_str_freq == s1_freq:
                return True      
            right += 1
            left += 1

        return False