


class Node:
    def __init__(self , val):
        self.val = val
        self.next = None




class Sll:
    head = None
    def insert_at_first(self,data):
        newnode = Node(data)
        if self.head is not None:
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = newnode

    def insert_at_end(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = newnode
    
    def reverse(self,root):
        prev = None
        cur = root
        while cur is not None:
            n = cur.next
            cur.next = prev 
            prev = cur
            cur = n
        
        return prev


n1 = Sll()
n1.insert_at_first(3)
n1.insert_at_first(2)
n1.insert_at_first(1)

n1.insert_at_end(4)

n1.head = n1.reverse(n1.head)
x = n1.head
while x is not None:
    print(x.val)
    x = x.next





