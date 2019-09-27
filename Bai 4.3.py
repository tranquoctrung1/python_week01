import random

def rollADice():
    while True:
        num =  random.randint(1,6)
        print(f'The number of a dice is: {num}')
        isContinue = input('Do you want to continue(y/n): ')
        if isContinue != 'y' and  isContinue != 'Y' and isContinue != 'yes' and isContinue != 'YES':
            break

rollADice()