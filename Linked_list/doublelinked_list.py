class Node(object):
    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is none")
        print("List is : ")
        p = self.start
        while p is not None:
            print(p.info," ", end = "")
            p = p.next
        print()

    def insert_begining(self,data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty(self,data):
        temp = Node(data)
        self.start = temp

    def insert_at_end(self,data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        data = int(input("Enter the first element to be inserted"))
        self.insert_in_empty(data)
        for i in range(n-1):
            data = int(input("Enter the next element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
                p = p.next
            if p is None:
                print(x," not presen in the list ")
            else:
                temp.prev = p
                temp.next = p.next
                if p.next is not None:
                    p.next.prev = temp
                p.next = temp;

    def insert_before(self,data,x):
        if self.start is None:
            print("List is empty")
            return

        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return

        p = self.start;
        while p is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_fiest_node(self):
        pass

    def delete_last_node(self):
        pass

    def delete_node(self,x ):
        pass

    def reverse_list(self):
        pass




