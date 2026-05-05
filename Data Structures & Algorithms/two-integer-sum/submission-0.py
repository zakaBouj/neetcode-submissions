class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        seen = {}
        seen[nums[0]] = 0

        for i in range(1, nums_len):
            if (target - nums[i]) in seen:
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i