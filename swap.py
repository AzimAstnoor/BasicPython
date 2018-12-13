x = float(input('Enter number1:'))
y = float(input('Enter number2:'))
a = float(input('Enter number3:'))
b = float(input('Enter number4:'))
c = float(input('Enter number5:'))
d = float(input('Enter number6:'))
temp = x
x = d
d = temp
y = y + c
c = y - c
y = y - c
a = a * b
b = a / b
a = a / b
print('The number1 after swap is', x)
print('The number2 after swap is', y)
print('The number3 after swap is', a)
print('The number4 after swap is', b)
print('The number5 after swap is', c)
print('The number6 after swap is', d)