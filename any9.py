try:
    a = []
    for b in range(6):
        q = int(input('Enter the Value'))
        a.append(q)
    print(a)
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)
except Exception as e: print(e)