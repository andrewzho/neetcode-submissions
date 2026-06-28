class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None
        self.length = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1
        

    def pop(self) -> None:
        self.stack = self.stack[0:self.length-1]
        self.length -= 1
        

    def top(self) -> int:
        return self.stack[self.length-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        
