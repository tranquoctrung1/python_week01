def totalIntDecimalInTuple(tupleTmp):
    sum = 0
    for item in tupleTmp:
        if isinstance(item, int) or isinstance(item, float):
            sum += item
    
    return sum

def main():
    tuple= (1, 2.3, 'alo')

    print(f'Sum = {totalIntDecimalInTuple(tuple)}')

    return 0

main()