
def maxNumber(a, b, c):
    maxNumber = a
    if b > a and b >c:
        maxNumber = b
    elif c > b and c > a:
        maxNumber = c
    
    print(f'Max  of Prime Number: {maxNumber}')

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

maxNumber(a, b, c)