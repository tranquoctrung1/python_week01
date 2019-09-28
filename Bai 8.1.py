def createATuple ():
    list = []
    while 1:
        x = input('Enter value: ')
        list.append(x)

        isContinue = input('Do you want to continue (y/n):')

        if isContinue != 'y':
            break
    tupleTmp = tuple(list)
    return tupleTmp

def main():
    tuple= ()

    tuple= createATuple()

    print(f'Tuple: {tuple}')

    return 0

main()
    

