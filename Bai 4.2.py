def isPrime(a):
    check = 0
    for x in range(1, a + 1):
        if a % x  == 0:
            check +=1
    if check == 2:
        return 1
    return 0

def totalPrime(n):
    sum =0
    for x in range(1,n +1 ):
        if isPrime(x) == 1:
            sum += x

    return sum

print(f'Sum = {totalPrime(100)}')