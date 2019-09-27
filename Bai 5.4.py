listInt = [1, 2, 3, 4, 7, 5, 6]
listInt2 = [0, 10, 20, 30, 1, 50]

def checkDuplicateElement(listInt, listInt2):
    check = 0

    for item in listInt:
        if item in listInt2:
            check += 1
    return check

def main():

    if checkDuplicateElement != 0:
        print(f'There is dulicate item in two list!!')
    else:
        print(f'There is not dulicate item in two list!!')
    return 0

main()