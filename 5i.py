try:
    a = input('Enter the String')
    a = a.split()
    b = a[0]
    d = a[0]
    c = d = len(a[0])
    for i in a:
        if len(i) > c:
            c == len(i)
            b = i
    for i in a:
        if len(i) < c:
            c == len(i)
            d = i
    print(b)
    print(d)
except Exception as e: print(e)