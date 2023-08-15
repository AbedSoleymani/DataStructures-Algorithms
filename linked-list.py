class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def prepend(self, data):
        """Insertion at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, target):
        if not self.head:
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next


if __name__ == "__main__":
    import os
    os.system("clear")

    print("basic approach:")
    head = Node(2) 
    head.next = Node(1)
    head.next.next = Node(4)
    print(head.next.next.data)

    print("\nadvanced approach:")
    my_linked_list = LinkedList()
    my_linked_list.append(data=1)
    my_linked_list.append(data=7)
    my_linked_list.append(data=3)
    my_linked_list.display()

    my_linked_list.prepend(data=-8)
    my_linked_list.display()

    search_result = my_linked_list.search(target=7)
    print(search_result)

    my_linked_list.delete(target=1)
    my_linked_list.display()