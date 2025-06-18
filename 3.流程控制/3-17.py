n = int(input())
for i in range(n):
    bmi = int(input())
    if bmi < 18.5:
        print("體重過輕")
    elif bmi>=18.5 and bmi < 24:
        print("正常")
    elif bmi>=24 and bmi < 28:
        print("體重過重")
    else :
        print("肥胖")
