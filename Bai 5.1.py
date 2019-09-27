listDecimal = [1.2, 2.3, 3.4, 4.5]

def total (listDecimal):
    sum =0
    for item in listDecimal:
        sum += item
    
    return sum

print(f'Sum = {total(listDecimal)}')