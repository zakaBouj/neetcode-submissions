class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        output = 0

        for num in nums:
            if num - 1 not in nums_set:
                curr = num
                new_output = 1
                while curr + 1 in nums_set:
                    curr += 1
                    new_output += 1
                
                output = max(output, new_output)

        return output