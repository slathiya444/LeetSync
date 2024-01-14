class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # occ_word1 = collections.Counter(word1)     
        # occ_word2 = collections.Counter(word2)  

        # print(sorted(occ_word1))
        # print(sorted(occ_word2))
        def find_occ(string: str):
            occ = collections.Counter(string)
            return (sorted(occ.keys()), sorted(occ.values()))

        return find_occ(word1) == find_occ(word2)
