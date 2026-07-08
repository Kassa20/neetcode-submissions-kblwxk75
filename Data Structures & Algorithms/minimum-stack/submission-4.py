class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) > 0: 
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        
        self.stack.append(val)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

        
