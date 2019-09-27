def total(n):
    sum = 0
    for x in range(1,n):
        sum += x

    return sum

    
n = int(input('Enter n: '))
print(f'Sum = {total(n)}')