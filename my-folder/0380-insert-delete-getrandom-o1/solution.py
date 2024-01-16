class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        idx = len(self.list)
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = idx
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            ## remove from list
            id_to_remove = self.dict[val]
            last = self.list[-1]

            self.list[id_to_remove] = last
            self.dict[last] = id_to_remove

            self.list.pop()

            ## remove from dictionary
            del self.dict[val]

            return True
        return False

        
    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
