from collections import deque

def bfs(adj, start=0):
    v = len(adj)
    res = []
    q = deque()
    vis = [False] * v

    vis[start] = True
    q.append(start)

    while q:
        x = q.popleft()
        res.append(x)

        for i in adj[x]:
            if not vis[i]:
                vis[i] = True
                q.append(i)

    return res


# Example graph
adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
print("BFS starting from 0:", bfs(adj, 0))
print("BFS starting from 2:", bfs(adj, 2))
