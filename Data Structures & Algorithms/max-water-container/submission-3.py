class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        max_vol = 0

        while left < right:
            current_vol = min(heights[left], heights[right]) * (right - left)
            max_vol = max(max_vol, current_vol)

            if heights[left] < heights[right] or heights[left] == heights[right]:
                left += 1
            else:
                right -= 1

        return max_vol