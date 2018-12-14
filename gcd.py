x = float(input('Enter Number1'))
y = float(input('Enter Number2'))
while y != 0:
  x, y = y, x % y
print(x)
