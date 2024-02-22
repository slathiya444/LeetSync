class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapp = defaultdict(int)

        for p, j in trust:
            mapp[j] += 1
            mapp[p] -= 1

        for person in range(1, n+1):
            if mapp[person] == n-1:
                return person

        return -1
