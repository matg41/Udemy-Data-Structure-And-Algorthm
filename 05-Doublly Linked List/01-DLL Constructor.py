class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            raise ValueError("Linked List is empty!")
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 10
            return True

    def pop_first(self):
        if self.length == 0:
            raise ValueError("Linked List is empty!")  
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.prev = None
            self.length -= 1
            return temp    
    def get(self, index):
        if index >self.length or index<0:
            return None
        else:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        new_node = Node(value)
        if index>self.length or index<0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        after = self.get(index)
        before = after.prev
        if after and before:
            new_node.next = after
            new_node.prev = before
            after.prev = new_node
            before.next = new_node
            self.length += 1
            return True
        return False

    def remove_value(self, index):
        if index >= self.length or index<0:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        after = temp.next
        before = temp.prev
        after.prev = before
        before.next = after
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
        

DLL = DoublyLinkedlist(1)
DLL.append(2)
DLL.append(3)
DLL.append(4)
DLL.print_list()
print("-----")
DLL.insert_value(8 , 6)
#DLL.print_list()
