"""
[11,32,45,78,89]
so for enque operation we append an element at the end i.e.after 89 using append
for deque operation we would delete the operation from front i.e.11 using pop
"""

#This approach has a disadvantage that if we perform a lot of enque and deque the list will have lot
# of None values.So use Circular Queue for that.

class EmptyQueueError(Exception):
    pass
class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def is_empty(self):
        return self.front == len(self.items)

    def size(self):
        return len(self.items)-self.front

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.items[self.front] = None
        self.front = self.front + 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        return self.items[self.front]

    def display(self):
        print(self.items)





