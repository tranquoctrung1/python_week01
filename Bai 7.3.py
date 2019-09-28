def removeDictionary(dict, key):
    del dict[key]
    return dict

def main():
    dict = {
        'ban': "Đạo",
        'tui': "Trung"
    }

    key = input('Enter the key:')

    print(f'Dictionary after remove the key {key} is: {removeDictionary(dict, key)}')

    return 0

main()