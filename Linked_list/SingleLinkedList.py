class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is: ")
            p= self.start
            while p is not None:
                print(p.info, "", end = '')
                p = p.link
            print()

    def count_nodes(self):
        p =self.start
        n = 0
        while p is not None:
            n=n+1
            p=p.link
            print("Number of nodes in list are {}".format(n))

    def search(self,x):
        position = 1
        p = self.start
        while p is not None:
            if p.info==x:
                print("{} is at position {}".format(x,position))
                return True
            position = position+1
            p=p.link
        else:
            print("{} not found in the list".format(x))
            return False


    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p=p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the data to be inserted:"))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        """If list is empty"""
        if self.start is None:
            print("List is empty")
            return
        """x is in first node, new node is to be inserted before first node"""
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        """Find the reference to predecessor of node containing x"""
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp


    def insert_at_position(self, data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        p = self.start
        i = 1

        if p is None:
            print("You can only insert upto position{} ".format(i))
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self,x):
        if self.start is None:
            print("List is empty")
            return
        # Deletion of first node
        if self.start.info ==x:
            self.start = self.start.link
            return
        # Deletion in between or at end
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print("Element {} is not present".format(x))
        else:
            p.link = p.link.link


    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None
            return
        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
            self.start = prev

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info,q.info = q.info,p.info
                    p=p.link
                end = p

    def bubble_sort_exlinks(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p!=self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q = q,p

                r = p
                p = p.link
                end = p

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self):
        pass

    def merge2(self,list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self,listStart):
        pass
    def _divide_list(self, p):
        pass