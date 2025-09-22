class Node:
    def __init__(self , val):
        self.val = val
        self.next = None



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

print(n1.val,n2.val,n3.val)

n1.next = n2
n2.next = n3

print(n1.next.val)