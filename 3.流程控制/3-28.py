n = int(input())
def isprime(n):
    if n <= 1:
        return False  
    if n == 2:
        return True   
    if n % 2 == 0:
        return False  

    for i in range(3, int(n ** 0.5) + 1, 2):  
        if n % i == 0:
            return False
    return True

print("odd" if n%2 == 1 else "even",end = "")
print(" prime" if isprime(n) else"")
