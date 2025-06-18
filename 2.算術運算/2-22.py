a = int(input())
if a>=0:
    print(bin(a)[2:].zfill(8))
else :
    print(bin(256+a)[2:].zfill(8))
