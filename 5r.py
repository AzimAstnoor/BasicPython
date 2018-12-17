try:
    i = int(input('Enter the no.'))
    a = []
    for i in range(0, i):
        b = int(input('Enter the no.'))
        a.append(b)
        i = i - 1
        m = []
    for x in a:
        if x%2 != 0:
            m.append(x)
    print(m)
except Exception as Z:  print(Z)