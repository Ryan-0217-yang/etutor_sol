n = input()
num = list(map(int , n))
for i in range(len(num)):
    for _ in range(num[i]):
        print("*",end = "")
    print() 
