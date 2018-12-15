try:
    i = 10
    a = []
    while i > 0:
        b = int(input('Enter the number'))
        a.append(b)
        i = i - 1
    c = int(input('Enter the number'))
    i = 9
    d = 0
    while i >= 0:
        if c == a[i]:
            print('The Number is Present.')
            d = d + 1
        i = i - 1
    if d == 0:
        print('The Number is not Present.')

except Exception as e: print(e)