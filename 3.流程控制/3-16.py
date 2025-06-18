n = int(input())
a = int((n/100)) ** 3
b = int(((n%100)/10)) ** 3
c = (n%10) ** 3
if n == a + b + c:
    print("YES")
else :
    print("NO")
