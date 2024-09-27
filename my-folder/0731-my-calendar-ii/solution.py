class MyCalendarTwo:

    def __init__(self):
        self.non_overlaping = []
        self.overlaping = []

    def book(self, start: int, end: int) -> bool:

        for s, e in self.overlaping:
            if not(e <= start or end <= s):
                return False

        for s, e in  self.non_overlaping:
            if not(e <= start or end <= s):
                self.overlaping.append((max(s, start), min(e, end)))
        self.non_overlaping.append((start, end))
        return True

        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
