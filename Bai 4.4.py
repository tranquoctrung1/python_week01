import math

def factorialCalc(a):
    total = 1
    for x in range(1, a):
        total *= x

    return total

def S(x, n):
    sum = x
    for i in range(2, n + 1):
        sum +=float(pow(x,i)) / float(factorialCalc(i))

    return sum

x = int(input('Enter x: '))
n = int(input('Enter n: '))

print(f'S = {S(x, n)}')