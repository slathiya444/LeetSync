class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(job_index, day):
            ### Base cases
            # on the last day, we have to finish all remaining jobs
            if day == d:
                # return hardest_job_remaining[job_index]
                return max(jobDifficulty[job_index:])

            ### recurrance relation
            # for a day day, if we choose to take a job, if we dont, then cost will be the previous cost
            # but if we are choosing the next jobs, we have to be careful because, 
            # there should be atleast one job left for every remaining days.
            # hence for the next selection, we have choices till 
            # remaining no of jobs = d
            cost = 0
            res = float("inf")
            for j in range(job_index, n-(d-day)):
                cost = max(cost, jobDifficulty[j])
                res = min(res, cost + dp(j+1, day+1))

            return res

        n = len(jobDifficulty)
        # if days are greater then no of jobs, we can not assign at least one job a day
        if n<d:
            return -1
        
        return dp(0, 1)


        
