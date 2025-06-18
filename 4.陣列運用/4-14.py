n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
mindiff = total

def dfs(index, mysum):
    global mindiff
    if index == n:
        diff = abs(total - 2*mysum)
        mindiff = min(mindiff, diff)
        return
    dfs(index+1, mysum + arr[index])
    dfs(index+1, mysum)

dfs(0, 0)
print(mindiff)
