a , b , c = sorted(map(int, input().split()))
com = input()
if com == "Asc":
    print(f"{a}<{b}<{c}")
else:
    print(f"{c}>{b}>{a}")
