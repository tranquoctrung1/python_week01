def removeACharacterOfString(string, n):
    if len(string) == 0:
        return ""
    else:
        if len(string) < n:
            print(f'n is larger than lenght of string!!')
            return string
        elif n < 0: 
            print(f'n is not negative!!')
            return string
        else:
            if n < len(string):
                return string[0:n -1 ] + string[n - len(string): -1] + string[-1]
            else: 
                return string[0:n -1 ]

def main():
    string = "Trung"
    n = int(input('Enter n: '))
    print(f'String after remove element: {removeACharacterOfString(string,n)}')

    return 0

main()
