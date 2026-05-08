class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums)
        
        freq_list = [[] for _ in range(len(nums) + 1)]

        for num in nums_freq:
            freq_list[nums_freq[num]].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in freq_list[i]:
                if k == 0:
                    break
                result.append(num)
                k -= 1

        return result