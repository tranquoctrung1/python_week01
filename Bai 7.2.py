def findKeyInDictionary(dict, key):
    if key in dict:
        print(f'Key is already exist and with value: {dict[key]}')
    else:
        print(f'Key is not in the dictionnary!!')

def main():
    dict = {
        'ban': "Đạo",
        'tui': "Trung"
    }

    key = input('Enter the key: ')
    findKeyInDictionary(dict, key)

main()