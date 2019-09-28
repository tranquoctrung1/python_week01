def removelastElement(tupleTmp):
    return tupleTmp[0: len(tupleTmp) -1 ]

def main():
    tuple = (1,2,3,4)

    print(f'Tuple after remove last element: {removelastElement(tuple)}')

    return 0

main()
    