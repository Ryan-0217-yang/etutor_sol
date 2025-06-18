n = int(input())
coin = list(map(int,input().split()))
total = int(input())
solution = []

def dfs(index , money , sol):
    if money > total:
        return 
    if index == n:
        if money == total:
            solution.append(sol[:])
        return
    
    maxcount = (total - money) // coin[index]

    for i in range(maxcount+1):
        sol.append(i)
        dfs(index+1 , money + i * coin[index] , sol)
        sol.pop()

dfs(0,0,[])
for sol in solution:
    print("(", end="")
    print(",".join(map(str, sol)), end="")
    print(")")
    

