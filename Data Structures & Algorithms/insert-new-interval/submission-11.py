class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals:
            if newInterval[1] < intervals[0][0]:
                res = [newInterval]
            elif newInterval[0] > intervals[0][1]:
                res = [intervals[0]]
            else:
                res = [[min(newInterval[0], intervals[0][0]), max(newInterval[1], intervals[0][1])]]
        else:
            return [newInterval]
        print(res)
        i = 0
        while i < len(intervals):
            # merge newInterval if overlapping with last interval from res
            if res[-1][1] >= newInterval[0]:
                res[-1] = [res[-1][0], max(res[-1][1], newInterval[1])]
            # append newInterval if right place and non-overlapping with last interval from res
            elif newInterval[0] <= intervals[i][0]:
                res.append(newInterval)

            # merge next interval if overlapping with last interval from res
            if res[-1][1] >= intervals[i][0]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            # append next interval if non-overlapping with last interval from res
            else:
                res.append(intervals[i])
            i += 1

        if res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1] = [res[-1][0], max(res[-1][1], newInterval[1])]

        return res




            # intervals = [[1,2],[3,7],[10,13]], newInterval = [6,11]
            # intervals = [[1,2],[3,7],[10,13]], newInterval = [8,9]
            # intervals = [[1,2],[3,7],[10,13]], newInterval = [8,10]