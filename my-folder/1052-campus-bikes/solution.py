class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        w = len(workers)
        b = len(bikes)
        distance = collections.defaultdict(list)

        for i in range(w):
            for j in range(b):
                d = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                distance[d].append((i, j))

        print(distance)

        bike_used = set()
        worker_used = set()
        ans = [None] * w

        for i in sorted(distance.keys()):
            for w, b in distance[i]:
                if w not in worker_used and b not in bike_used:
                    bike_used.add(b)
                    worker_used.add(w)
                    ans[w] = b

        return ans
