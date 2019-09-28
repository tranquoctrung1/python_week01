def removeAElementInTuple(tupleTmp, location):
    listTmp = list( tupleTmp )

    del listTmp[location]

    tupleTmp = tuple(listTmp)

    return tupleTmp

def main():
    tuple = (1,2,3,4)

    location = int(input('Enter location: '))

    print(f'Tuple after remove a specified element: {removeAElementInTuple(tuple, location)} ')

    return 0

main()