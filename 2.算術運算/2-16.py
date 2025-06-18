starth, startm = input().split(" ")
endh, endm = input().split(" ")
starth = int(starth)
startm = int(startm)
endh = int(endh)
endm = int(endm)

total_min = (endh - starth) * 60 + (endm - startm)
part = int(total_min/30)
if part <= 4:
    print(part *30)
elif part > 4 and part <= 8:
    print((part - 4) * 40 + 120)
else : 
    print((part -8) * 60 + 280)
