class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        track = {}
        for winner, looser in matches:
            track[winner] = track.get(winner, 0)
            track[looser] = track.get(looser, 0) + 1

        zero = []
        one = []

        for item in sorted(track.items(), key=lambda x:x[1]):
            if item[1] >1:
                break
            if item[1] == 0:
                 zero.append(item[0])
                 continue
            one.append(item[0])

        return [sorted(zero), sorted(one)]


        
