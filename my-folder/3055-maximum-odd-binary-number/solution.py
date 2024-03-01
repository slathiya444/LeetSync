class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones
        res = ''

        # build the result
        # to make the number odd, last bit have to be '1'
        # hence (ones-1)*'1' + all zeros + '1' is the result

        # add (ones-1) 1's
        for _ in range(1, ones):
            res += '1'

        # add zeros
        for _ in range(zeros):
            res += '0'

        # add last 1 to make it odd
        res += '1'
        return res  

        
