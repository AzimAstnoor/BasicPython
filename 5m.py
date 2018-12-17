try:
    a = input('Enter the String:')
    b = a.capitalize()
    c = a.lower()
    d = a.upper()
    i = 2
    f = []
    for i in range(0, 3):
        j = input('Enter New String')
        f.append(j)
        i = i - 1
    print(b, '\n', c, '\n', d, '\n', f)
except Exception as e: print(e)