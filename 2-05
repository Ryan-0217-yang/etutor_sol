a, b = map(int, input().split())

print(f"{a}+{b}={a + b}")
print(f"{a}*{b}={a * b}")
print(f"{a}-{b}={a - b}")

q = int(a / b)  
r = a - b * q
if r < 0:
    r += b
    q += -1   
if r == 0:
    print(f"{a}/{b}={q}")
else:
    print(f"{a}/{b}={q}...{r}")
