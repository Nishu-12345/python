class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def display_backward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=' ')
            temp = temp.prev
        print()
        
        #  add this block to excute someting when script is run
        
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    
    print("forward traversal:")
    dll.display_forward()

    print("backward traversal:")
    dll.display_backward()
        # dll = DoublyLinkedList()
        # dll.append(10)
        # dll.append(20)
        # dll.append(30)

        # dll.display_forward()   # Output: 10 20 30
        # dll.display_backward()  # Output: 30 20 10
