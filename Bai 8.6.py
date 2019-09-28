def removeDuplicateElements(tupleTmp):
    listTmp = list(tupleTmp)

    for item in listTmp:
        check = 0
        for item2 in listTmp:
            if item2 == item:
                check += 1
        if check >= 2:
            listTmp.remove(item)
    
    tupleTmp= tuple(listTmp)

    return tupleTmp

def main():
    tuple =  ('a', 2, 'b', 2, 'a', 'c', 'a')

    print(f'Tuple after remove duplicate elements: {removeDuplicateElements(tuple)}')

    return 0

main()