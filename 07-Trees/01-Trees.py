class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                elif new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right
    
    def contains(self, value):
        if self.root is None:
            return False
        else:
            temp = self.root
            while temp is not None:
                if temp.value == value:
                    return True
                elif value < temp.value:
                    temp = temp.left
                else :
                    temp = temp.right
                
        return False

my_tree = BST()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(3))
