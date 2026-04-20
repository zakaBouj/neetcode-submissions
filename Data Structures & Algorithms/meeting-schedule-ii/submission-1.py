"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        day_to_endTime = {}

        for interval in intervals:
            start = interval.start
            end = interval.end
            
            if not day_to_endTime:
                day_to_endTime[0] = end
                continue

            for day in day_to_endTime:
                print(day_to_endTime[day])
                print(start)
                if day_to_endTime[day] <= start:
                    day_to_endTime[day] = end
                    break
            else:
                day_to_endTime[len(day_to_endTime)] = end

        return len(day_to_endTime)