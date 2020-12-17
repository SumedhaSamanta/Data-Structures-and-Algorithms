class unionFind:
    def __init__(self,n):
        self.n = n+1
        self.p = [-1]*(n+1)
        self.p[0] = 'X'
    def find(self,x):
        if self.p[x]<0:
            parent = x
        else:
            parent = self.p[x]
        size_of_parent = abs(self.p[parent])
        return parent,size_of_parent
    def union(self,x,y):
        p_x,size_x = self.find(x)
        p_y,size_y = self.find(y)
        if(p_x != p_y):
            if(size_x >= size_y):
                self.p[p_x] = self.p[p_x] - size_y
                self.p[p_y] = p_x
                for i in range(self.n):
                    if self.p[i] == p_y or self.p[i] == y:
                        self.p[i] = p_x
            if(size_x < size_y):
                self.p[p_y] = self.p[p_y] - size_x
                self.p[p_x] = p_y
                for i in range(self.n):
                    if self.p[i] == p_x or self.p[i] == x:
                        self.p[i] = p_y
    def display(self):
        print(self.p)
                
    
