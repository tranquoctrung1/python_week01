listInt = [1, 2, 3, 4, 7, 5, 6]

def total (listInt):
    sum = 0
    for item in listInt:
        if item % 2 == 0:
            sum += item

    return sum

print(f'Sum = {total(listInt)}')