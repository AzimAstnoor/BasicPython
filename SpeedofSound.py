import math
a = float(input('Enter tHe Coefficent of Stiffness:'))
b = float(input('Enter tHe Density of Air:'))
c = math.sqrt(a/b)
d = c * 1234.8
print('The speed of sound in mach is', c)
print('The speed of sound in km/hr is', d)