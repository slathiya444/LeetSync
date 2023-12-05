class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## can add open if open < n
        ## can add close only if close < open
        ## valid iff open == close == n

        stack = []
        res = []

        def backtracking(opn, close):
            if opn == close == n:
                res.append("".join(stack))
                return

            if opn < n:
                stack.append('(')
                backtracking(opn+1, close)
                stack.pop()

            if close < opn:
                stack.append(')')
                backtracking(opn, close+1)
                stack.pop()

        backtracking(0,0)

        return res
        
