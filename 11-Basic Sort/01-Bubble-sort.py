import random
import time
def bSort(l):
    new_l = []
    for _ in range(len(l)):
        for i in range(len(l)):
            #print('stage:',i,'\n')
            if len(l)==1:
                new_l.append(l.pop())
                return new_l[::-1]
            if i<len(l)-1:
                a = l[i]
                b = l[i+1]
                if a>b:
                    l[i]=b
                    l[i+1]=a
            else:
                new_l.append(l.pop())
            #print(l)

def bSort_2(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
in_l = []
for i in range(10000):
    in_l.append(round(random.random()*100))
print(in_l)
t1 = time.time()
n_l = bSort(in_l)
#print(n_l)
t2 = time.time()
print(t2-t1)
in_l = []
for i in range(10000):
    in_l.append(round(random.random()*100))
t1 = time.time()
n_l = bSort_2(in_l)
print(n_l)
t2 = time.time()
print(t2-t1)

        