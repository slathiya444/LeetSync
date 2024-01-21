class Solution:
    def minimumPushes(self, word: str) -> int:
        mapp = collections.Counter(word)

        chars = sorted(mapp.items(), key = lambda x: x[1])

        total, iteration = 0, 1

        current = 0
        for char, value in chars:
            if current == 8:
                current = 0
                iteration += 1

            total += value*iteration
            current+=1

        return total
        
