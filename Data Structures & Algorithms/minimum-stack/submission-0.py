class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_num:
            self.min_num.append(min(self.min_num[-1], val))
        else:
            self.min_num.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]
