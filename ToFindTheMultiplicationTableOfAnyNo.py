a = float(input('Enter the Number you want the multiplication table'))
d = float(input('Enter the N. you want to find the multiplaction table till'))
c = 1
while c < d:
    b = a*c
    print(c, ' * ', a, ' = ', b)
    c = c + 1