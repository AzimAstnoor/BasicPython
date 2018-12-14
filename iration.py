print('1. First\n'
      '2. Second')
a = float(input('your the type of input'))
if a == 2:
    b = input('type your name to match it with the list')
    c = ['q','c','t','a','n','x','o','r','w','e','l','u']
    if b in c:
        print('You are Allowed in 2nd Hall ')
    else:
        print('YOU ARE NOT ALLOWED')
if a == 1:
    b = input('type your 3-digit password to match it with the list')
    c = [124,546,789,345,654,486,154,348,357,486,157,579]
    if b in c:
        print('You are welcomed to the 1st Hall')
    else:
        print('YOU ARE NOT ALLOWED')