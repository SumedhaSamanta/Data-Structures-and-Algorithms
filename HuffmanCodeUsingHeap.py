import math
def insertForMinHeap(b,k):
    b.append(k)
    c = len(b) - 1
    p = math.ceil(c/2) - 1
    while(p>=0 and c>0 and b[p][1]>b[c][1]):
        b[p],b[c] = b[c],b[p]
        c = p
        p = math.ceil(c/2) - 1
        
def heapsortUsingMinHeap(a):
    l = len(a)
    item = []
    merge = {}
    metasymbols = {}
    last = 0
    lastsymbol = ""
    for i in range(l):
        merge[str(i)]=[str(i),w[i],0]
    while(l>0):
        b = []
        for i in list(merge.keys()):
            insertForMinHeap(b,merge[i])
        b[0],b[l-1]=b[l-1],b[0]
        item.append(b.pop())
        #print(item)
        del merge[item[-1][0]]
        if len(item)==2:
            item1 = item[0]
            item2 = item[1]
            merge[(str(item1[0])+str(item2[0]))] = [(str(item1[0])+str(item2[0])),item1[1]+item2[1],max(item1[2],item2[2])+1]
            metasymbols[(str(item1[0])+str(item2[0]))] = [str(item1[0]),str(item2[0])]
            last = max(item1[2],item2[2])+1
            lastsymbol = (str(item1[0])+str(item2[0]))
            insertForMinHeap(b,merge[(str(item1[0])+str(item2[0]))])
            item = []
            
        l = len(merge)
        if(l==0):
            print(last)
            break
        print("Current state of merge dictionary:")
        print(merge)
    print("All the metasymbols:")
    print(metasymbols)
    sym = metasymbols[lastsymbol]
    sym1 = sym[0]
    sym2 = sym[1]
    c = 1
    while(sym1 in metasymbols.keys() and sym2 in  metasymbols.keys()):
            print("Last symbol:")
            print(lastsymbol)
            print("Components:")
            print(sym)
            #print(c)
            if len(sym1)>len(sym2):
                lastsymbol = sym2
            else:
                lastsymbol = sym1
            sym = metasymbols[lastsymbol]
            sym1 = sym[0]
            sym2 = sym[1]
            c = c + 1
    print(c)
                
       
n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
heapsortUsingMinHeap(w)
