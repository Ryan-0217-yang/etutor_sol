n = int(input())
girl = list(map(str,input().split()))
like = input()
likearr = list(map(int, like))

sum = 0
for i in range(n):
    girlarr = list(map(int, girl[i]))
    if set(likearr).issubset(set(girlarr)): 
        sum += 1

print(sum)
