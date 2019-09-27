def removeElmentOddIndex(string):
    newString = ""
    index = 0
    for item in string:
        if index %2 == 0:
            newString +=item
        index+=1

    return newString

def main():
    string = "Txrxuxnxgxx"

    print(f'String after remove odd elements: {removeElmentOddIndex(string)}')

    return 0

main()