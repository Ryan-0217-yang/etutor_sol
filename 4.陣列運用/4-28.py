a, b = input().split(",")
arr = list(map(int, a))
b = int(b)

min_num = []
start = 0
length = len(arr) - b

for i in range(length):
    end = len(arr) - length + i + 1
    min_val = min(arr[start:end])
    min_num.append(min_val)
    start = arr.index(min_val, start) + 1  

print("".join(map(str, min_num)))
