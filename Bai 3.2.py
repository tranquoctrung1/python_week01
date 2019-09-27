def convertCDegree(fDegree):
    cDegree = 5 * (fDegree - 32) / 9
    print(f'C: {cDegree}')

fDegree = float(input('Enter F Degree: '))
convertCDegree(fDegree)