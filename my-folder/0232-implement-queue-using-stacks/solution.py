class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
    
    def helper_push(self):
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        # if pop stack is empty, 
        #check push stack and push all elements from push stack to pop stack in reverse
        # so that pop operation will end up being O(1)
        if not self.pop_stack:
            self.helper_push()
        return self.pop_stack.pop()

    def peek(self) -> int:
        if not self.pop_stack:
            self.helper_push()
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
