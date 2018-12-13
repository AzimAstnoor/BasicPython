import math
a = float(input('Enter the side of square'))
a **=a
b = float(input('Enter the length of rectangle'))
c = float(input('Enter the width of rectangle'))
d = (b+c)**2
e = float(input('Enter the 1st side of triangle'))
f = float(input('Enter the 2nd side of tirangle'))
g = float(input('Enter the 3rd side of triangle'))
h = (e+f+g)/2
i = h*(h-e)*(h-f)*(h-g)
j = float(input('Enter the radius of circle'))
k = 3.14*(j**2)
l = float(input('Enter the no. of sides'))
m = float(input('Enter the length of side'))
n =(l*(m**2))/4
o = n/math.tan(3.14/l)
print('The area of square',a)
print('the area of rectngle',d)
print('The area of triangle',math.sqrt(i))
print('The area of circle is',k)
print('The area of Regular n-polygon is',o)