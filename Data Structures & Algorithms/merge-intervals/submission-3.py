class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting intervals base on start value of each interval
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        # merge intervals 
        res = [sorted_intervals[0]]
        i = 1
        while i < len(sorted_intervals):
            if i < len(sorted_intervals):
                if res[-1][1] >= sorted_intervals[i][0]:
                    res[-1] = [res[-1][0], max(res[-1][1], sorted_intervals[i][1])]
                else:
                    res.append([sorted_intervals[i][0], sorted_intervals[i][1]])
            else:
                res.append([sorted_intervals[i][0], sorted_intervals[i][1]])
            i += 1

        return res

