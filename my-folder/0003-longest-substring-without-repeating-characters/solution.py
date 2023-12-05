class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        ans = 0
        visited = set()

        while(j<len(s)):

            if s[j] not in visited:
                visited.add(s[j])
                j += 1
                ans = max(len(visited), ans)
            
            else:
                visited.remove(s[i])
                i+=1
        
        return ans


        
