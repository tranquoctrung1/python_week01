def createAString(string):
    if len(string) < 2:
        return ""
    else: 
       return string[0:2] + string[-2] + string[-1]

def main():
    string = "w3c"

    print(f'Creating new string: {createAString(string)}')

main()