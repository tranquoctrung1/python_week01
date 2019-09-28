def insertTuple(tupleTmp, value, location):
    listTmp = list(tupleTmp)

    if len(listTmp) == location:
        listTmp.append(value)
    else:
        listTmp.insert(location, value)
    
    tupleTmp = tuple(listTmp)

    return tupleTmp

def main():
    tuple = (1,2,3,4)

    value = int(input('Enter value: '))
    location = int(input('Enter location: '))

    print(f'Tuple after insert with location {location} and value {value}: {insertTuple(tuple, value, location)}')

    return 0

main()