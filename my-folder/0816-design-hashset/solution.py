class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for i in range(self.size)]
        
    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hash = self._hash(key)
        bucket = self.bucket[hash]

        for item in bucket:
            if item == key:
                return
        bucket.append(key)

    def remove(self, key: int) -> None:
        hash = self._hash(key)
        bucket = self.bucket[hash]
        for item in bucket:
            if item == key:
                bucket.remove(item)
        return 
        
    def contains(self, key: int) -> bool:
        hash = self._hash(key)
        bucket = self.bucket[hash]
        for item in bucket:
            if item == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
