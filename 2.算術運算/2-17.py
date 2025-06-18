hour, salary = input().split(" ")
hour = int(hour)
salary = int(salary)

if hour <= 60:
    print("%.1f"%(hour * salary))
elif hour > 60 and hour <= 120:
    print("%.1f"%((hour - 60) * salary * 1.33 + 60 * salary))
else : 
    print("%.1f"%((hour - 120) * salary * 1.66 + 60 * salary * 1.33 + 60 * salary))
