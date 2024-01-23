

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        record = set()

        def is_valid(record, s):
            c = Counter(record) + Counter(s)
            return max(c.values()) > 1

        lru_cache(None)
        def dp(index):
            ## base cases
            if index == len(arr):
                return len(record)

            res = 0

            ## recurance relation
            # if we take the current arr element
            # check if any repearing chars
            if not is_valid(record, arr[index]):
                for char in arr[index]:
                    record.add(char)
                res = dp(index+1)
                # remove previous elements characters if we decide not to take them
                for char in arr[index]:
                    record.remove(char)

            # if we do not take current arr element
            return max(res, dp(index+1))

        return dp(0)


        
