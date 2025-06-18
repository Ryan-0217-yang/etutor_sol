n = int(input())
arr = list(map(int , input().split()))
addn = int(input())

arr.append(addn)
arr.sort()
print(",".join(map(str,arr)))
