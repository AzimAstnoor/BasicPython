try:
    q =int(input('Enter the number'))
    a = []
    while q > 0:
        num = int(input('Enter the number'))
        a.append(num)
        q = q - 1
    print(a)
    for i in range(0, len(a)):
      for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
    print(a)
except Exception as e: print(e)