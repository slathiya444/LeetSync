class Solution:
    def isValid(self, s: str) -> bool:
        start = ['(', '{', '[']
        end = [')', '}', ']']
        additional = []
        mapp = dict(zip(end, start))
        for i in s:
            if i in start:
                additional.append(i)
            elif i in end and additional:
                if additional.pop() != mapp.get(i):
                    return False
            else:
                return False
        if not additional:
            return True
        
