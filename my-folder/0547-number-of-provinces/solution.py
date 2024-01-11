class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for city_city in range(len(isConnected)):
                if isConnected[city][city_city] == 1 and city_city not in visited:
                    dfs(city_city)

        p = 0
        visited = set()
        for city in range(len(isConnected)):
            if city not in visited:
                p += 1
                dfs(city)

        return p

        
