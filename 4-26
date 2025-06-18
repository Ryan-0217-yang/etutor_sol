n, m = map(int, input().split())  

matrix = []  
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

tran_matrix = [[0] * n for _ in range(m)]

for i in range(n):      
    for j in range(m):  
        tran_matrix[j][i] = matrix[i][j]


for row in tran_matrix:
    print(" ".join(map(str, row)))

