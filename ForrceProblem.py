import math
f1 = float(input('Enter force1'))
f2 = float(input('Enter force2'))
f3 = float(input('Enter force3'))
m = float(input('Enter mass'))
h = float(input('Enter Height'))
net: float = f1 + f2 + f3
a = net / m
g = m * 9.8
w = m*g*h
u = net/f3
print('The net force is', net)
print('The accrelation is', a)
print('The gravity is', g)
print('The work done is', w)
print('The coeffiecnt of friction',u)

