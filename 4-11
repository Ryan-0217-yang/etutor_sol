arr = [0]*5
n = int(input())

for i in range(n):
    grade = int(input())
    if grade == 100:
        arr[4] += 1
    elif grade < 60:
        arr[0] += 1
    else:
        arr[grade//10 - 5] += 1

print(f"優等 {arr[4]}")
print(f"甲等 {arr[3]}")
print(f"乙等 {arr[2]}")
print(f"丙等 {arr[1]}")
print(f"不及格 {arr[0]}")
