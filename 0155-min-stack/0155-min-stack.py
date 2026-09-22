from collections import deque

class MinStack(object):

    def __init__(self):
        self.sub = deque()
        self.min_sub = deque()

    def push(self, value):
        self.sub.append(value)

        if not self.min_sub:
            self.min_sub.append(value)
        else:
            self.min_sub.append(min(value, self.min_sub[-1]))

    def pop(self):
        self.sub.pop()
        self.min_sub.pop()

    def top(self):
        return self.sub[-1]

    def getMin(self):
        return self.min_sub[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()