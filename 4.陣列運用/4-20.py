n = input()
m = input()
flag = False
for i in range(len(m)-len(n)+1):
    if n == m[i:i+len(n)]:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")
