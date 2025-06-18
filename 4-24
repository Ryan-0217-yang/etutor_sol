n = int(input())
feeling = []
for i in range(n):
    row = list(map(int, input().split()))
    feeling.append(row)

boy = [False]*n
girl = [False]*n
for k in range(n):
    maxfeeling = 0
    maxb = 0
    maxg = 0
    for i in range(n):
        if not boy[i]:
            for j in range(n):
                if not girl[j]:
                    if maxfeeling < feeling[i][j]:
                        maxfeeling = feeling[i][j]
                        maxb = i
                        maxg = j
    print(f"boy {maxb+1} pair with girl {maxg+1}")
    boy[maxb] = True
    girl[maxg] = True
