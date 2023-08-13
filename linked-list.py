# %%

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
   
head = Node(2) 
head.next = Node(1)
head.next.next = Node(4)

print(head.value)
print(head.next.next.value)

# %%
from collections import deque
my_deque = deque(maxlen=100)