def totalIntDictionary(dictionary):
    sum = 0
    for x in dictionary.values():
        if isinstance(x, int):
            sum += x

    return sum

def main():

    dictionary ={
        '1': 2,
        '2': 3,
        '3': 4.5,
        '4': 'Hello'
    }

    print(f'Sum = {totalIntDictionary(dictionary)}')

    return 0

main()
