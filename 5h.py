try:
    a = input('Enter the letter')
    a = a.split()
    b = a[0][0] + "." + a[1][0] + "." + a[2][0] + "."
    print(b)
except Exception as e: print(e)