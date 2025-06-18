n ,turn= input().split()
n = int(n)
matrix = [[0]*n for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        matrix[i][j] = num
        num += 1

turn_matrix = [[0]*n for _ in range(n)]
if turn == 'L':
    for i in range(n):
        for j in range(n):
            turn_matrix[i][j] = matrix[j][n-1 - i]
elif turn == 'R':
    for i in range(n):
        for j in range(n):
            turn_matrix[i][j] = matrix[n-1-j][i]
else :
    for i in range(n):
        for j in range(n):
            turn_matrix[i][j] = matrix[n-1 - i][j]

for row in turn_matrix:
    print(" ".join(map(str,row)))
