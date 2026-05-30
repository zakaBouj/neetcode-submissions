class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 1
        res.append(max(nums[0:k]))

        for right in range(k,len(nums)):         
            res.append(max(nums[left:right+1]))
            left += 1

        return res