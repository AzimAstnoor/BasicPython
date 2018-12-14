print('How many no. do you want to use: '
      '2 '
      '3 '
      '4  ')
x = float(input('Enter the no. number you are using'))
if x ==2:
    print('which operator do you wanna use: '
          '1. Addition '
          '2. Subtraction '
          '3. Multiplication '
          '4. Division '
          '5. Modulus '
          '6. Power ')
    e = float(input('Enter the No. beside the operator u want to use '))
    if e ==1:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        f = a+b
        print(f)
    elif e == 2:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        f = a - b
        print(f)
    elif e == 3:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        f = a * b
        print(f)
    elif e == 4:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        f = a / b
        print(f)
    elif e == 5:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        f = a % b
        print(f)
    else:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        f = a ** b
        print(f)
elif x ==3:
    print('which operator do you wanna use: '
          '1. Addition '
          '2. Subtraction '
          '3. Multiplication '
          '4. Division '
          '5. Modulus '
          '6. Power ')
    e = float(input('Enter the No. beside the operator u want to use '))
    if e ==1:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        f = a+b+c
        print(f)
    elif e == 2:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        f = a - b - c
        print(f)
    elif e == 3:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        f = a * b * c
        print(f)
    elif e == 4:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        f = a / b / c
        print(f)
    elif e == 5:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        f = a % b % c
        print(f)
    else:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        f = (a ** b) ** c
        print(f)
elif x == 4:
    print('which operator do you wanna use: '
          '1. Addition '
          '2. Subtraction '
          '3. Multiplication '
          '4. Division '
          '5. Modulus '
          '6. Power ')
    e = float(input('Enter the No. beside the operator u want to use '))
    if e ==1:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        d = float(input('Enter number D'))
        f = a+b+c+d
        print(f)
    elif e == 2:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        d = float(input('Enter number D'))
        f = a - b - c - d
        print(f)
    elif e == 3:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        d = float(input('Enter number D'))
        f = a * b * c * d
        print(f)
    elif e == 4:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        d = float(input('Enter number D'))
        f = a / b / c / d
        print(f)
    elif e == 5:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        d = float(input('Enter number D'))
        f = a % b % c % d
        print(f)
    else:
        a = float(input('Enter number A'))
        b = float(input('Enter number B'))
        c = float(input('Enter number C'))
        d = float(input('Enter number D'))
        f = ((a ** b) ** c) ** d
        print(f)