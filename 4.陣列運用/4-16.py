n = int(input())
bus = [0]*24
for i in range(n):
    s , d = map(int,input().split()) 
    for i in range(s-1,d-1):
        bus[i] += 1
print(max(bus))
