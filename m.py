i = 0
j = 9
for row in range(5):
    for col in range(11):
        if col == 0 or col == 10or (row==col-1) :
            print('*', end='')
        elif (col == j and row == i ) :
            print('*', end = '')
            i = i + 1
            j = j - 1
        else:
            print(end=' ')
    print()