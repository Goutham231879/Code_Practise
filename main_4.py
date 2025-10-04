def addEdge(i, j, mat):
    mat[i].append(j)
    

def display(mat):
    for i in range(len(mat)):
        print(f"{i} -> ", end="")
        for j in mat[i]:
            print(j, end=" ")
        print("")


def transpose(mat, tran):
    for i in range(len(mat)):
        for j in mat[i]:
            tran[j].append(i)   # Reverse the direction of edge


# Number of vertices
v = 5

# Original and transpose adjacency lists
mat = [[] for _ in range(v)]
tra = [[] for _ in range(v)]

# Add edges
addEdge(0, 1, mat) 
addEdge(0, 4, mat) 
addEdge(0, 3, mat) 
addEdge(2, 0, mat) 
addEdge(3, 2, mat) 
addEdge(4, 1, mat) 
addEdge(4, 3, mat)

print("Original Graph:")
display(mat)

# Build transpose
transpose(mat, tra)

print("\nTranspose Graph:")
display(tra)
