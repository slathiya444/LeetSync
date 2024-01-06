class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        cache = {}
        intervals = sorted(zip(startTime, endTime, profit))

        def dfs(i):

            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            ## do not consider ith job
            res = dfs(i+1)

            ## consider ith job
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            # while j < len(intervals):
            #     if intervals[i][1] <= intervals[j][0]:
            #         break
            #     j+= 1 
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)
        
