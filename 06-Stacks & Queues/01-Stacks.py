
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value) -> bool:
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.height += 1
            return True
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    def pop(self) -> object:
        if self.height==0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -=1
        return temp



my_stack = Stack(0)
my_stack.push(1)
my_stack.push(2)
my_stack.print_stack()
print("-------")
my_stack.pop()
my_stack.print_stack()
print("-------")
my_stack.pop()
my_stack.print_stack()
print("-------")
my_stack.pop()
my_stack.print_stack()

