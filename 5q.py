try:
    i = int(input('Enter the no.'))
    a = []
    for i in range(0, i):
        b = int(input('Enter the no.'))
        a.append(b)
        i = i - 1
    d = set()
    u = []
    for x in a:
        if x not in d:
            u.append(x)
            d.add(x)
    print(d)
except Exception as Z: print(Z)