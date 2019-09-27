def getSeason(month):
    if month < 1 or month > 12:
        print('Invalid month')
    elif month <= 3:
        print('Spring')
    elif month <= 6:
        print('Summer')
    elif month <= 9:
        print('Autumn')
    elif month <= 12:
        print('Winter')

month = int(input('Enter month: '))
getSeason(month)