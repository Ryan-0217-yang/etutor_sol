arr = list(map(int , input().split(",")))
maxarr = sorted(arr , reverse=True)
minarr = sorted(arr)
maxsum = 0
minsum = 0

for i in range(len(arr)):
    maxsum += maxarr[i] * (10 ** (len(arr) - 1 - i))
    minsum += minarr[i] * (10 ** (len(arr) - 1 - i))
print(maxsum - minsum)
