class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            for j in range(len(temperatures) - i):
                if temperatures[j + i] > temperatures[i]:
                    res.append(j)
                    break
            if len(res) == i:
                res.append(0)

        return res