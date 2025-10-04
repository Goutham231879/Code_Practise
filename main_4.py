#bfs
from collections import deque
def bfs(mat, src):
    vis = [False]*len(mat)
    q=deque()
    q.append(src)
    vis[src]=True
    while q:
        x = q.popleft()
        print(x,end=" ")
        for i in mat[x]:
            if not vis[i]:
                q.append(i)
                vis[i]=True





mat =[[1,2], [0,2,3], [0,1,4], [1,4], [2,3]]

src = 1

print("bfs of the graph")
bfs(mat,src)