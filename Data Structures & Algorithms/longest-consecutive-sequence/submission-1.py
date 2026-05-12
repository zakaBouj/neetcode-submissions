class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        for num in nums:
            current_seq = 1
            current_num = num + 1
            
            while current_num in nums_set:
                current_seq += 1
                current_num += 1
            
            max_seq = max(max_seq, current_seq)
                
        return max_seq