n , m= input().split()
sum = 0
for i in range(len(m)-len(n)+1):
    if n == m[i:i+len(n)]:
        sum += 1
print(sum)
