try:
    a = int(input('Enter the Lower range:'))
    b = int(input('Enter the Upper range:'))
    i = []
    square = []
    e = []
    for i in range(a, b):
        e = i**2
        square.append(e)
        i = i + a
    print(square)
except Exception as e:print(e)
