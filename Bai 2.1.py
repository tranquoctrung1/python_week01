a = int(input('Enter a:'))
b = int (input('Enter b:'))

if a == 0:
    if b == 0:
        print(f'Phuong tring vo so nghiem')
    else:
        print(f'Phuong trinh vo nghiem')
else:
    print(f'Phuong trinh co 1 nghiem duy nhat la: {-b}/{a}')
