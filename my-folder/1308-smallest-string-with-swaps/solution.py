class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        p = [i for i in range(len(s))]

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                p[py] = px

        for pair in pairs:
            union(pair[0], pair[1])

        dd = defaultdict(list)
        
        for idx, element in enumerate(p):
            dd[find(element)].append(idx)
        res = list(s)
        for key in dd.keys():
            id_list = dd[key]
            characters = [s[i] for i in id_list]
            characters.sort()

            for id, val in zip(id_list, characters):
                res[id] = val

        return "".join(res)

        
