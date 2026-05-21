class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        maxLeft = list()
        for num in height:
            if not maxLeft or num > maxLeft[-1]:
                maxLeft.append(num)
            else:
                maxLeft.append(maxLeft[-1])

        maxRight = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                maxRight[i] = height[i]
            else:
                maxRight[i] = max(height[i], maxRight[i + 1])

        for i in range(len(height)):
            res += min(maxLeft[i], maxRight[i]) - height[i]

        return res