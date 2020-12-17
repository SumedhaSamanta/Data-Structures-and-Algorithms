import math
class Prims:
    V = []
    #E = []
    X = []
    T = []
    A = []
    heap = []
    Cost = 0
    def insertForMinHeap(self,k):
        self.heap.append(k)
        print(self.heap)
        c = len(self.heap) - 1
        p = math.ceil(c/2) - 1
        while(p>=0 and c>0 and self.heap[p][1]>self.heap[c][1]):
            self.heap[p],self.heap[c] = self.heap[c],self.heap[p]
            c = p
            p = math.ceil(c/2) - 1
    def heapsortUsingMinHeap(self,B):
        l = len(B)
        print(l)
        while(l>0):
            for i in B.keys():
                print(str(i)+str(B[i]))
                self.insertForMinHeap([i,B[i]])
            self.heap[0],self.heap[l-1]=self.heap[l-1],self.heap[0]
            item = self.heap.pop()
            print(item)
            self.X.append(item[0])
            self.Cost = self.Cost + item[1]
            l = len(self.heap)
            B = {self.heap[i][0]: self.heap[i][1] for i in range(0, len(self.heap))}
            self.heap = []
            return B
        
    def PrimsAlgo(self):
        self.X.append(1)
        B = {}
        for i in self.V:
            if i not in self.X:
                B[i] = 999999999
        while(len(self.V)>len(self.X)):
            print("X: ")
            print(self.X)
            e = self.X[-1]
            print("e = "+str(e))
            for v in self.V:
                if v not in self.X:
                    print(v)
                    print(self.A[e-1][v-1])
                    B[v] = min(B[v],self.A[e-1][v-1])
            print("B: ")
            print(B)
            B = self.heapsortUsingMinHeap(B)
            print(self.Cost)
            
    def inputGraph(self):
        Vn = int(input("Enter the number of vertices:"))
        for i in range(Vn):
            self.V.append(i+1)
            self.A.append([])
            for j in range(Vn):
                self.A[i].append(9999999)
        En = int(input("Enter the number of edges:"))
        for i in range(En):
            u,v,w = map(int,input("Enter the 2 vertices and the edge between them; all three separated by space:").split())
            #self.E.append([u,v])
            #self.E.append([v,u])
            self.A[u-1][v-1] = w
            self.A[v-1][u-1] = w
        for i in range(Vn):
            for j in range(Vn):
                print(self.A[i][j],end="\t")
            print()
            
p1 = Prims()
p1.inputGraph()
p1.PrimsAlgo()
