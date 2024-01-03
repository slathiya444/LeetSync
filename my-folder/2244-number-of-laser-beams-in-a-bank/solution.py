class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0

        for floor in bank:
            count = 0
            for cell in floor:
                if cell == "1":
                    count += 1

            if count > 0:
                ans = ans + (count*prev)
                prev = count

        return ans
