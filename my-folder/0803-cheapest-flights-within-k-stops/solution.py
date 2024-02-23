class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')] * n
        price[src] = 0
        for i in range(k+1):
            tmpPrice = price.copy()

            for s, d, c in flights:
                if price[s] == float('inf'):
                    continue
                tmpPrice[d] = min(tmpPrice[d], price[s] + c)

            price = tmpPrice

        return -1 if price[dst] == float('inf') else price[dst]
