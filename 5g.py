try:
    c = "bcdfghklmnpqrstwvyxzBCDFGHKLMNPQRSTWVYXZ"
    v = " aeiouAEIOU"
    w = " "
    a = input('Enter the String')
    b = 0
    d = 0
    e = 0
    for i in a:
        if i in c:
            b = b + 1
        if i in v:
            d = d + 1
        if i in w:
            e = e + 1
    print('The number of Consonents is ', b)
    print('The number of Vowels is ', d)
    print('The number of White Space is ', e)
except Exception as z: print(z)