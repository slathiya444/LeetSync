

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)
        sum = 0
        while q:
            q.popleft() # for bob
            q.pop() # for Alice
            sum += q.pop()
        return sum
        
