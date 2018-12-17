try:
    a = input('Enter the String')
    w = a.split()
    w.sort()
    for w in w:
        print('\n', w)
except Exception as e: print(e)