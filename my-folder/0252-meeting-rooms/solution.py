class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # first sort by start time
        sorted_intervals = intervals.sort(key = lambda x:x[0])

        for idx in range(len(intervals)-1):
            if intervals[idx][1] > intervals[idx+1][0]:
                return False

        return True
        
