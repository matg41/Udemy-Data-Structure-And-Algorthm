
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_nod = Node(value)
        if self.length == 0:
            self.tail = new_nod
            self.head = new_nod
        else:
            new_nod.next = self.head
            self.head = new_nod
        self.length += 1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length ==0:
            self.tail = None
        return temp
    def get(self, index):
        if index > self.length:
            raise ValueError(f"{index} is out of range")
        if index<0:
            raise ValueError("Index must not be negative")
        if self.length == 0:
            return None
        temp = self.head
        for i in range(0,index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index > self.length:
            raise ValueError(f"{index} is out of range")
        if index<0:
            raise ValueError("Index must not be negative")
        if index == 0:
            self.prepend(value)
            
        elif index == self.length:
            self.append(value)
            
        else:
            temp_pre = self.get(index-1)
            temp_after = self.get(index)
            new_node = Node(value)
            temp_pre.next = new_node
            new_node.next = temp_after
            self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next=before
            before = temp
            temp = after
        return True

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
print("len=",ll.length)
#print(ll.get(0))
#print(ll.get(3).value)
ll.print_list()
#ll.insert(4,15)
ll.reverse()
print("len=",ll.length)
print("-------------")
ll.print_list()
    

