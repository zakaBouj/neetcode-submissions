class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        left = 0
        right = len(s1) - 1
   
        sub_str_freq = defaultdict(int)
        sub_str_freq = Counter(s2[left : right])
        print(sub_str_freq)

        while right < len(s2):
            sub_str_freq[s2[right]] += 1
            
            if sub_str_freq == s1_freq:
                return True         
            
            sub_str_freq[s2[left]] -= 1
            if sub_str_freq[s2[left]] == 0:
                del sub_str_freq[s2[left]]

            right += 1
            left += 1

        return False