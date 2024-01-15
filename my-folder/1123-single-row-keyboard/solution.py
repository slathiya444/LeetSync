class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        charDict = {}

        for i in range(26):
            charDict[keyboard[i]] = i

        time = charDict[word[0]]

        for i in range(len(word) - 1):
            idx1 = charDict[word[i]]
            idx2 = charDict[word[i + 1]]
            distance = abs(idx1 - idx2)
            time += distance

        return time

        
