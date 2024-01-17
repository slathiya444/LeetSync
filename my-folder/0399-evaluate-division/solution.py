class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = {}

        def find(x):
            if x not in dic:
                dic[x] = (x, 1)

            group, weight = dic[x]
            if x != group:
                new_group, new_weight = find(group)
                dic[x] = (new_group, new_weight * weight)
            return dic[x]

        def union(x, y, weight):
            g1, w1 = find(x)
            g2, w2 = find(y)

            if g1 != g2:
                dic[g1] = (g2, weight*w2/w1)

        res = []
        for (dividend, divisor), weight in zip(equations, values):
            union(dividend, divisor, weight)

        for dividend, divisor in queries:
            if dividend not in dic or divisor not in dic:
                res.append(-1)
                continue

            if dividend == divisor:
                res.append(1)
                continue

            g1, w1 = find(dividend)
            g2, w2 = find(divisor)

            if g1 == g2:
                res.append(w1 / w2)
            else:
                res.append(-1)

        return res

        
        
