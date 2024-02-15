class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []

        remove = toBeRemoved
        for start, end in intervals:
            ## check if no overlap of interval with removed
            if end < remove[0] or start > remove[1]:
                res.append([start, end])

            ## check overlaping cases
            else:
                # check if start should be in output:
                if start < remove[0]:
                    res.append([start, remove[0]])
                # check if end should be kept in output
                if end > remove[1]:
                    res.append([remove[1], end])

        return res
        

        return res
