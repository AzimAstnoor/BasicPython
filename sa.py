for row in range(8):
    for col in range(9):
        if (row == 0 and col>0)\
            or (row == 3 and col>0 and col<8)\
            or (row == 6 and col<8)\
            or(col == 0 and (row > 0 and row < 3 ))\
            or(col == 8 and (row > 3 and row < 6)):
            print('*', end=' ')
        else:
            print(end='  ')
    print()

i = 0
j = 4
for row in range(6):
    for col in range(9):
        if (row == col-4 and col>4)\
                or(row==2 and (col>2 and col<6)):
            print('*',end = ' ')
        elif row == i and col == j:
            print('*', end=' ')
            i = i + 1
            j = j - 1
        else:
            print(end = '  ')
    print()

for row in range(8):
    for col in range(9):
        if (row == 6 and col<8 and col>0)\
            or (col == 0 and row<6)\
            or (col == 8 and row<6):
            print('*', end=' ')
        else:
            print(end='  ')
    print()

for row in range(8):
    for col in range(9):
        if (row == 0 and col < 8) or (row == 3 and col < 8) or (col == 0 and row<7) or (col == 8 and row<3 and row>0)\
            or (col == 2 and row == 4) or (col == 3 and row == 5) or (col == 4 and row == 6):
            print('*', end=' ')
        else:
            print(end='  ')
    print()

i = 0
j = 4
for row in range(6):
    for col in range(9):
        if (row == col-4 and col>4)\
                or(row==2 and (col>2 and col<6)):
            print('*',end = ' ')
        elif row == i and col == j:
            print('*', end=' ')
            i = i + 1
            j = j - 1
        else:
            print(end = '  ')
    print()

for row in range(8):
    for col in range(9):
        if (row == 0 and col<8) or row == 3 or (row == 6 and col<8) or (col == 0 and row<7) or (col == 8 and row<6 and row>0):
            print('*', end=' ')
        else:
            print(end='  ')
    print()

for row in range(8):
    for col in range(9):
        if row == 3 or (col == 0 and row < 8) or (col == 8 and row < 8):
            print('*', end=' ')
        else:
            print(end='  ')
    print()