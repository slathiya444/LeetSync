class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        required, window = {}, {}

        for char in t:
            required[char] = 1 + required.get(char, 0)

        have, need = 0, len(required)

        res, res_len = [-1, -1], float("infinity")

        l=0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in required and window[ch] == required[ch]:
                have += 1

            while have == need:

                ## update the result
                if (r-l+1) < res_len:
                    res = [l, r]
                    res_len = (r-l+1)

                ## remove element from left to moving the window
                window[s[l]] -= 1
                if s[l] in required and window[s[l]] < required[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""
            


