class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # n = len(s)
        # ans = -1
        # for left in range(n):
        #     for right in range(left+1, n):
        #         if s[left] == s[right]:
        #             ans = max(ans, right - left - 1)

        # return ans

        index_map = {}
        ans = -1
        n = len(s)

        for char in range(n):
            if s[char] in index_map:
                ans = max(ans, char - index_map[s[char]] - 1)
            else:
                index_map[s[char]] = char

        return ans
