from decimal import Decimal, ROUND_HALF_UP

n = int(input())
for _ in range(n):
    w = Decimal(input())  
    ans = w * w
    print(ans.quantize(Decimal('0.1'), ROUND_HALF_UP))

