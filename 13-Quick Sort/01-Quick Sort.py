

def Swaping(my_list,index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp



def Pivot(my_list, p_index, e_index):
    swap_index = p_index

    for i in range(p_index+1, e_index+1):
        if my_list[i]< my_list[p_index]:
            swap_index += 1
            Swaping(my_list, swap_index, i)
    Swaping(my_list, p_index, swap_index)
    return swap_index

def Quick_Sort_Helper(my_list, left, right):
    if left < right:
        p_index = Pivot(my_list,left, right)
        Quick_Sort_Helper(my_list, left, p_index-1)
        Quick_Sort_Helper(my_list, p_index+1, right)
    return my_list

def Quick_Sort(my_list):
    return Quick_Sort_Helper(my_list, 0, len(my_list)-1)


l = [4,1,2,7,6,5,3]

print(Quick_Sort(l))