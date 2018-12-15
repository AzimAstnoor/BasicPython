try:
    i = 0
    j = 4
    for row in range(6):
        for col in range(9):
            if (row == col - 4 and col > 4) \
                    or (row == 2 and (col > 2 and col < 6)):
                print('*', end='')
            elif row == i and col == j:
                print('*', end='')
                i = i + 1
                j = j - 1
            else:
                print(end=' ')
        print()

    i = 0
    j = 5
    for row in range(7):
        for col in range(6):
            if (row == 5 and col > 0) or (row == 0 and col < 5):
                print('*', end=' ')
            elif (row == i and col == j):
                print('*', end=' ')
                i = i + 1
                j = j - 1
            else:
                print(end='  ')
        print()

    for row in range(8):
        for col in range(5):
            if row == 0 or (col == 2 and row < 7) or row == 6:
                print('*', end=' ')
            else:
                print(end='  ')
        print()

    i = 0
    j = 9
    for row in range(5):
        for col in range(11):
            if col == 0 or col == 10 or (row == col - 1):
                print('*', end='')
            elif (col == j and row == i):
                print('*', end='')
                i = i + 1
                j = j - 1
            else:
                print(end=' ')
        print()
except Exception as e: print(e)