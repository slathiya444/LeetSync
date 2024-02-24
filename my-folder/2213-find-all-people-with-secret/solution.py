class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        time = {}

        for src, dst, t in meetings:
            if t not in time:
                time[t] = defaultdict(list)
            time[t][src].append(dst)
            time[t][dst].append(src)

        def dfs(src, adj):
            if src in visited:
                return

            visited.add(src)
            secrets.add(src)

            for nei in adj[src]:
                dfs(nei, adj)

        for t in sorted(time.keys()):
            visited = set()
            for src in time[t]:
                if src in secrets:
                    dfs(src, time[t])

        return list(secrets)
        
