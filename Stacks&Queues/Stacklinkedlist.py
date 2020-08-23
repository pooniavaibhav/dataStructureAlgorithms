"""
In Linked list if we take the end of the list as top we have to traverse the whole list to reach at the
end and perform operation.
If we use top as starting we can easily add or remove element.
"""
class EmptyStackError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def size(self):
        if self.is_empty():
            return 0
        count = 0
        p = self.top
        while p is not None:
            count+=1
            p = p.link
        return count

    def push(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        popped = self.top.link
        return popped

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.top.info

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack is : ")
        p = self.top
        while p is not None:
            print(p.info , " ")
            p = p.link





