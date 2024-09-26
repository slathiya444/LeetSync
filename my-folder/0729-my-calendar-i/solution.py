class MyCalendar:

    def __init__(self):
        self.my_calender = [] # (s, e)
        

    def book(self, start: int, end: int) -> bool:
        for s, e in self.my_calender:
            if s < end and start < e:
                return False
        self.my_calender.append((start, end))
        return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
