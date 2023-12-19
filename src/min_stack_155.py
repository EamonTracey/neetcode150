# Design a stack that supports push, pop, top, and
# retrieving the minimum element in constant time.
# 
# Implement the MinStack class: 
# 1. MinStack() initializes the stack object.
# 2. void push(int val) pushes the element val onto the stack.
# 3. void pop() removes the element on the top of the stack.
# 4. int top() gets the top element of the stack.
# 5. int getMin() retrieves the minimum element in the stack.
#
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    def __init__(self):
        self.elements = []
        self.mins = []

    def push(self, val: int) -> None:
        self.elements.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        if self.elements.pop() == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.mins[-1]

