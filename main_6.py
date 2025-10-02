def add_mat(mat , i , j):
    mat[i].append(j)
    mat[j].append(i)


def display(mat):

    for i in range(len(mat)):
        print(i,':',end=" ")
        for j in mat[i]:
            print(j,end=" ")
        print()

    print()

v = 4

mat = [ []  for _ in range(v   )]

add_mat(mat,0,1)
add_mat(mat,0,2)
add_mat(mat,1,2)
add_mat(mat,2,3)


display(mat)



