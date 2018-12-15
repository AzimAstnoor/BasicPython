try:
    a = int(input('Enter the Lower range:'))
    b = int(input('Enter the Upper range:'))
    even = []
    odd = []
    four = []
    six = []
    eight = []
    ten = []
    three = []
    five = []
    seven = []
    nine = []
    i = []
    for i in range(a, b):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for i in even:
        if i % 4 == 0:
            four.append(i)
        if i % 6 == 0:
            six.append(i)
        if i % 8 == 0:
            eight.append(i)
        if i % 10 == 0:
            ten.append(i)
    for i in odd:
        if i % 3 == 0:
            three.append(i)
        if i % 5 == 0:
            five.append(i)
        if i % 7 == 0:
            seven.append(i)
        if i % 9 == 0:
            nine.append(i)
    print(even)
    print(odd)
    print(three)
    print(four)
    print(five)
    print(six)
    print(seven)
    print(eight)
    print(nine)
    print(ten)
except Exception as e: print(e)