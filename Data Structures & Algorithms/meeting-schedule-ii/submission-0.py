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
        day_end_times = []

        for meeting in intervals:
            day_found = False

            for i in range(len(day_end_times)):
                if day_end_times[i] <= meeting.start:
                    day_end_times[i] = meeting.end
                    day_found = True
                    break

            if not day_found:
                day_end_times.append(meeting.end)
        
        return len(day_end_times)