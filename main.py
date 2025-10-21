from collections import deque
def dfs(gp , vis , st):
    vis[st] = True
    print(st)
    for x in gp[st]:
        if not vis[x]:
            vis[x] =True
            dfs(gp , vis , x)
    
def bfs(gp , st):
    d = deque()
    vis = [False]*(len(gp)+1)
    d.append(st)
    vis[st] = True

    while d :
        q = d.popleft()
        print(q)
        for x in gp[q]:
            if not vis[x]:
                d.append(x)
                vis[x]=True


n = 4
gp = [[] for _ in range(n+1)]
gp[1].append(2)
gp[1].append(3)
gp[2].append(4)
gp[3].append(4)

print("bfs")
bfs(gp , 1)

vis = [False] * (n+1)
print("dfs")
dfs(gp , vis , 1)