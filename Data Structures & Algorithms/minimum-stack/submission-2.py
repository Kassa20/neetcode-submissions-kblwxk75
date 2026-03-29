class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.minVal = 2**31 - 1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minVal:
            self.min_stack.append(val)
            self.minVal = val

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.stack.pop()
            self.min_stack.pop()
            self.minVal = self.min_stack[-1] if len(self.min_stack) != 0 else 2**31 - 1
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
