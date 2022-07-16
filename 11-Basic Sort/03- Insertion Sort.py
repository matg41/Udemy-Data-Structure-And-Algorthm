import time
import random
def inserteionSort(l):
    for i in range(1,len(l)):
        temp = l[i]
        j = i-1
        while temp < l[j] and j > -1:
            l[j+1] = l[j]
            l[j] = temp
            j -= 1
    return l



in_l = []
for i in range(10000):
    in_l.append(round(random.random()*100))
print(in_l)
t1 = time.time()
n_l = inserteionSort(in_l)
print(n_l)
t2 = time.time()
print(t2-t1)