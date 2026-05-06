class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagram_groups = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in anagram_groups:
                anagram_groups[sorted_string] = [string]
            else:
                anagram_groups[sorted_string].append(string)

        return list(anagram_groups.values())