try:
    i = int(input('Enter the length of list'))
    a = []
    while i > 0:
        num = int(input('Enter the number'))
        a.append(num)
        i = i - 1
    print(a)
    i = 0
    l = a[0]
    while i < len(a):
        if l < a[i]:
            la = a[i]
            li = i
        i = i + 1
    print(li)
    sl = a[0]
    i = 0
    while i < len(a):
        if l != a[i] and sl < a[i]:
            sl = a[i]
        i = i + 1
    diff = l - sl
    print(a[:li] + [sl, diff] + a[li + 1:])
except Exception as e: print(e)