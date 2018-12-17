try:
    i = 9
    a = []
    for i in range(0, 10):
        b = input('Enter the name of your friend')
        a.append(b)
        i = i-1
    a.sort()
    print(a)
except Exception as e: print(e)