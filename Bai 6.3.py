def additionString(string):
    if len(string) < 3:
        return string
    else:
        if (string[-3: -1 ] + string[-1]) == "ing":
            return string + "ly"
        else:
            return string + "ing"

def main():
    string = "string"

    print(f'String after additon: {additionString(string)}')

    return 0

main()

