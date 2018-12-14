i = 0
j = 4
for row in range(10):
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
