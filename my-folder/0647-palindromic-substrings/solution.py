class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        pick the element(i), and check around,
        if element in left (i-1) and in right (i+1) is same,
        then there is new palindrom string.
        Same for even number of strings
        pick 2 elements, if they are same, expand in left and right as above
        '''
        res = 0
        for i in range(len(s)):
            # for odd length palindrom strings
            res += self.findPalindrom(s, i, i)

            ## for even length, left and right will be different
            res += self.findPalindrom(s, i, i+1)

        return res

    def findPalindrom(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
