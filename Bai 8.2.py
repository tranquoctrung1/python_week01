def appendTuple(tupleTmp, value):
    listTmp = list(tupleTmp)
    listTmp.append(value)

    tupleTmp= tuple(listTmp)
    return tupleTmp

def main():
    tuple = (1,2,3,4,5)

    value = int(input('Enter value you want insert: '))

    print(f'Tuple after insert value {value}: {appendTuple(tuple, value)}')

    return 0

main()

