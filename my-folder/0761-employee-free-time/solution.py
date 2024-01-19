"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        ints = []
        for i in schedule:
            [ints.append(x) for x in i]

        ints.sort(key = lambda x: x.start)
        
        merged = []

        for interval in ints:
            if not merged or interval.start > merged[-1].end:
                merged.append(interval)

            else:
                merged[-1].end = max(interval.end, merged[-1].end)

        res = []
        for free_interval in range(1, len(merged)):
            res.append(Interval(start=merged[free_interval-1].end, end=merged[free_interval].start))

    
        return res

        
