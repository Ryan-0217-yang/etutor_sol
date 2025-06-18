n = int(input())
if n <= 800:
    print(n*0.9)
elif n>800 and n<1500:
    print("%.1f"%(n*0.9*0.9))
else:
    print("%.1f"%(n*0.9*0.79)) 
