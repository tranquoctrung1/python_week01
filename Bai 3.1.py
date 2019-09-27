import datetime

def yearOfBorn(year):
    now = datetime.datetime.now()
    print(f'Ban sinh nam: {year} va ban {now.year - year}')

year = int(input('Nhap nam sinh vao:'))
yearOfBorn(year)