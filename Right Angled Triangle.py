import math
a = float(input('Enter The Side1:'))
b = float(input('Enter The Side2:'))
c = math.hypot(a,b)
s = (a+b+c)/2
Perimeter = a+b+c
Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('The Perimeter of Right Angled Area', Perimeter)
print('The Area of Right Angled Area', Area)