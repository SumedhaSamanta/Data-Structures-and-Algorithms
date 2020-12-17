import math
class Heap:
    a = []
    n = 0
    heap = []
    def __init__(self,a,n):
        self.n = n
        self.a = a
        self.heap = []
    def insert(self,k):#insert element k into the existing heap; maintain heap property
        self.heap.append(k)
        c = len(self.heap) - 1
        p = math.ceil(c/2) - 1
        while(p>=0 and c>0 and self.heap[p][1]>self.heap[c][1]):#bubble-up
            self.heap[p],self.heap[c] = self.heap[c],self.heap[p]
            c = p
            p = math.ceil(c/2) - 1
    def heapify(self):
        for i in range(self.n):
            self.insert(self.a[i])
        #self.displayHeap()
    def extractMin(self):
        return self.deleteAtIndex(0)
    def deleteAtIndex(self,k):#delete element at index k of the heap
        self.heap[k],self.heap[-1]=self.heap[-1],self.heap[k]
        item = self.heap.pop()
        #print("item popped=",item)
        lenHeap = len(self.heap)
        p = k
        lc = (2*p) + 1
        rc = (2*p) + 2
        while((lc<lenHeap and self.heap[p][1]>self.heap[lc][1]) or (rc<lenHeap and self.heap[p][1]>self.heap[rc][1])):#bubble-down
            if rc>=lenHeap or self.heap[lc][1]<self.heap[rc][1]:
                self.heap[lc],self.heap[p] = self.heap[p],self.heap[lc]
                p = lc
            else:
                self.heap[rc],self.heap[p]= self.heap[p],self.heap[rc]
                p = rc
            lc = (2*p) + 1
            rc = (2*p) + 2
        #self.displayHeap()
        return item
    def deleteElement(self,k):#delete element k from the heap
        self.heap.remove(k)
        self.a = self.heap
        self.heap = []
        self.heapify()
        self.displayHeap()
    def displayHeap(self):
        print(self.heap)
        
#The above Heap class is used for faster implementation of Dijkstra's Algorithm
nV = int(input())#no of vertices
a = []
V = []
for i in range(nV):#input graph
    a.append([])
    V.append(i)
    l = [y for y in input().split()]
    u = int(l[0]) - 1
    for i in range(1,len(l)):
        v,w = map(int,l[i].split(','))
        a[u].append([v-1,w])
#print("a=",a)
dist = [1000000]*nV#to store the single source shortest paths
s = 1#source vertex is say,vertex 1
X = []
X.append(s-1)#to keep track of vertices already visited
dist[s-1] = 0
dd = []#a double dimensional array each element is stroing the vertex number and it's key (that is, so far computed shortest distance)
for i in range(nV-1):
    dd.append([(i+1),1000000])
h = Heap(dd,nV-1)#using heap data structure for fast implementation
h.heapify()
while(len(X)<len(V)):
    #print("X=",X)
    v = X[-1]
    #print("v=",v)
    adjv = a[v]
    #print("adjv=",adjv)
    for adj in adjv:
        vertex = adj[0]
        weight = adj[1]
        if dist[vertex]>dist[v]+weight:
            dd[vertex-1][1] = min(dd[vertex-1][1],dist[v]+weight)#updating keys of the objects in heap
    h.a = dd
    h.heap = []
    h.heapify()
    item = h.extractMin()
    X.append(item[0])
    if dist[item[0]]> item[1]:
        dist[item[0]]=item[1]
    dd[item[0]-1]=[item[0],1000000]
    #print("dd=",dd)
print("dist=",dist)
#print("dd=",dd)
#h.displayHeap()        
