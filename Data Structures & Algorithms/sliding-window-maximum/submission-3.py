class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        d = deque()

        for right in range(len(nums)):
            if d and d[0] < left:
                d.popleft()
            while d and nums[right] > nums[d[-1]]:
                d.pop()
            d.append(right)
            if right + 1 >= k:   # window is full
                res.append(nums[d[0]])
                left += 1

        return res