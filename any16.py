try:
    i = int(input('Enter the length of list'))
    a = []
    while i > 0:
        num = int(input('Enter the number'))
        a.append(num)
        i = i - 1
    print(a)
    b = [a[len(a) - 1]] + a[:len(a) - 1]
    print(b)
    a = b
    print(a)
except Exception as e: print(e)