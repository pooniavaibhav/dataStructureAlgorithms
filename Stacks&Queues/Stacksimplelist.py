"""
We know that in stack insertion and deletion is done only at one end which is called the
top of the stack.
[3,4,6,8]
In above list if we consider top before three at every pop and push we have to shift all the elements
left or right.
But if we consider top after 8 we need not to shift others.
"""

class EmptyStackError(Exception):
    pass

class StackFullError(Exception):
    pass

class Stack:
    def __init__(self,max_size):
        self.items = [None] * max_size
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.items == 0

    def is_full(self):
        return self.count == len(self.items)

    def push(self,x):
        if self.is_full():
            raise StackFullError("Stack is full, cant push")
        self.items[self.count] = x
        self.count+=1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty, cant pop")
        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count-=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty, cant peek")
        return self.items[self.count-1]

    def display(self):
        print(self.items)


