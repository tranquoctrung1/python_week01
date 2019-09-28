def addToDictionary(dict, key, value):
    dict[key] = value
    return dict

def main():
    dict  = {
        'thang': "Đạo",
        'tui': "Trung"
    }

    key = input('Enter the key: ')
    value = input('Enter the value: ')
    
    print(f'Dictionary after add: {addToDictionary(dict, key, value)}')

main()