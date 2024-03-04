class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res, score = 0, 0
        tokens.sort()
        l, r = 0, len(tokens)-1
        while l<=r:
            # play token face-up
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                res = max(res, score)
            # play token face-down
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1

            # return if none is possible
            else:
                break

        return res

        
