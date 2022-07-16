
def Merge(l1 , l2):
    L = []
    i = 0
    j = 0
    while (True):
        if i is not None and j is not None:
            if l1[i]<l2[j]:
                L.append(l1[i])
                i += 1
                if i >= len(l1):
                    i = None
            else:
                L.append(l2[j])
                j += 1
                if j >= len(l2):
                    j = None
            
        elif i is None:
               L.append(l2[j])
               j += 1
               if j >= len(l2):
                    j = None
        elif j is None:
             L.append(l1[i])
             i += 1
             if i >= len(l1):
                    i = None
        
        
        
        if i == None and j == None:
            return L


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return Merge(merge_sort(left), merge_sort(right))




l1 = [2,5,1,3,6,4,8,7,9]

print(merge_sort(l1))