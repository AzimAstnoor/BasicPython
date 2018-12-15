i = 10
a = []
while i>0:
  num = int(input('Enter the number'))
  a.append(num)
  i = i-1
print(a)
a.reverse()
b = a
print(b)
a.reverse()
print(a)