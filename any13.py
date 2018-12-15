i = int(input('Enter the length of list'))
a = []
while i > 0:
  num = int(input('Enter the number'))
  a.append(num)
  i = i-1
sum = sum(a)
print(a, '\n', sum)