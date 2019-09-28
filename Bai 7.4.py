def isEmptyDictionary(dict):
    if(len(dict) == 0):
        print("Dictionary is empty!!")
    else:
        print('Dictionary is not empty!!')

def main():
    dict ={
        'ban': "Đạo",
        'tui': "Trung"
    }

    isEmptyDictionary(dict)

    return 0

main()