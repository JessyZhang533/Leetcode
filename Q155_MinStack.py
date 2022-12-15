class MinStack(object):

    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))  # !!!: append a tuple into the stack: (the appended value, the min value when the current appended value is at the top of stack)
           
    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:  # otherwise return None
            return self.stack[-1][0]
        
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return float('inf')  # !!!


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
