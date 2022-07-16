class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1
        return True

    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.first
        if self.height == 1:
            self.first = None
            self.last = None        
        else:
            self.first = temp.next
            temp.next = None
            self.height -= 1
        return temp
        




queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()
print("\n")
queue.dequeue()
queue.print_queue()
