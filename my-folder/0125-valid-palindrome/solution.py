class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for char in s:
            if char.isalnum():
                st+=char

        return st.lower() ==  "".join(reversed(st.lower()))

        
