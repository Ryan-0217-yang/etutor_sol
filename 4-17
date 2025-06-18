n = input()
prime = []

def isprime(n):
    if n <= 1:
        return False  
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  

    for i in range(3, int(n**0.5) + 1, 2): 
        if n % i == 0:
            return False
    return True

for part in range(1,len(n)+1):
    for i in range(len(n)-part+1):
        sum = 0
        for j in range(i,i+part):
            sum += int(n[j])*(10 ** (i+part-j-1))
        if isprime(sum):
            prime.append(sum)

if prime:
    print(max(prime))
else:
    print("No prime found")

