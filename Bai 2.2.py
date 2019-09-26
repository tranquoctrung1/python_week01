import math

a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))

if a == 0:
    if b == 0 and c==0:
        print (f'Phuong trinh co vo so nghiem')
    else:
        print (f'Phuong trinh co 1 nghiem: {-b}/{c}')
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print(f'Phuong trinh vo nghiem')
    if delta == 0:
        print (f'Phuong trinh co nghiem kep: {-b}/ {a*2}')
    else:
        tmp_1 = (-b + math.sqrt(delta)) / (2*a)
        tmp_2 = (-b - math.sqrt(delta)) / (2*a)
        print (f'Phuong trinh co 2 nghiem phan biet: {tmp_1} và {tmp_2}')
