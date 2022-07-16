def funcTree():
    print("Tree")

def funcTwo():
    funcTree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")


def fac(n):
    if n==0 or n==1:
        return 1
    return n * fac(n-1)

print(fac(5))