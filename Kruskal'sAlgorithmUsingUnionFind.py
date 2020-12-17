nV = int(input())
nE = int(input())
E = []
for _ in range(nE):
    u,v,w = map(int,input().split())
    E.append([u-1,v-1,w])
E =sorted(E, key = lambda x : x[2])
print(E)
V = [-1]*nV
cost = 0
for e in E:
    u = e[0]
    v = e[1]
    w = e[2]
    lu = u
    lv = v
    while(V[lu]>=0):
        lu = V[lu]
    while(V[lv]>=0):
        lv = V[lv]
    if lu == lv:
        continue
    else:
        if(V[lu]<=V[lv]):
            V[lu] = V[lu] - 1
            V[v] = lu
            if v!=lv:
                V[lv] = lu
                V[lu] = V[lu] - 1
            for ver in range(nV):
                if V[ver] == v or V[ver]==lv:
                    V[lu] = V[lu] - 1
                    V[ver] = lu
        elif(V[lu]>V[lv]):
            V[lv] = V[lv] - 1
            V[u] = lv
            if u!=lu:
                V[lu]= lv
                V[lv] = V[lv] -1
            for ver in range(nV):
                if V[ver]==u or V[ver]==lu:
                    V[lv] = V[lv] - 1
                    V[ver] = lv
        cost = cost + w
    #print("V=")
    #print(V) 
print(cost)
