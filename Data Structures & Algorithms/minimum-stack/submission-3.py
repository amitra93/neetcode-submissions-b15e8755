class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        # print(f"pushed {val}, contents of stack is {self.stack}, minStack is {self.minStack}")

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        # print(f"popped, contents of stack is {self.stack}, minStack is {self.minStack}")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]