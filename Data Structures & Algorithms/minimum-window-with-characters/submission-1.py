class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = Counter(t)
        curr_freq = defaultdict(int)
        left = 0
        res = ""
        matches = 0
        needed_matches = len(t_freq)

        for right in range(len(s)):
            c = s[right]
            if c in t_freq:
                curr_freq[c] += 1
                if t_freq[c] == curr_freq[c]:
                    matches += 1

            while matches == needed_matches:
                if not res or len(res) > len(s[left:right+1]):
                    res = s[left:right+1]
                curr_freq[s[left]] -= 1
                if s[left] in t_freq and curr_freq[s[left]] < t_freq[s[left]]:
                    matches -= 1
                left += 1

        return res