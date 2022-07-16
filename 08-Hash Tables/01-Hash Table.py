from torch import le


class HT:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        return True 
    
    def get_item(self, key) -> int or None:
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
            return None
        return None

    def keys(self) -> list:
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
my_hash_table = HT()
my_hash_table.set_item("Ali", 15)
my_hash_table.set_item("Mehdi", 19)
my_hash_table.set_item("Mohammad", 10)
my_hash_table.set_item("Fati", 11)
my_hash_table.set_item("Arash", 18)


my_hash_table.print_table()
print("\n")
print(my_hash_table.get_item('Zahra'))
print(my_hash_table.keys())
