def item_in_commeo(list1, list2):
    D = {}
    for i in list1:
        D[i] = True
    for j in list2:
        if j in D:
            return True
    return False


print(item_in_commeo([1,2,3], [4,5,3]))