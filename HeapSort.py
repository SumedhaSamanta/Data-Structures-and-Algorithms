import math
def insertForMinHeap(b,k):
    b.append(k)
    c = len(b) - 1
    p = math.ceil(c/2) - 1
    while(p>=0 and c>0 and b[p]>b[c]):
        b[p],b[c] = b[c],b[p]
        c = p
        p = math.ceil(c/2) - 1
def heapsortUsingMinHeap(a):
    l = len(a)
    while(l>0):
        b = []
        for i in range(l):
            insertForMinHeap(b,a[i])
        b[0],b[l-1]=b[l-1],b[0]
        item = b.pop()
        print(item)
        l = len(b)
        a = b  
a=[30,59,27,69,7,67]
heapsortUsingMinHeap(a)
