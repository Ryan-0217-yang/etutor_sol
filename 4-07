n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):  
    fsum = sum(arr[:i])    
    bsum = sum(arr[-i:])   
    if fsum == bsum:
        count += 1

print(count)
