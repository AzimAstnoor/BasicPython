i = 0
j = 4
for row in range(5):
    for col in range(11):
        if (row == col-4 and col>4)or col==0 or col ==8:
            print('*',end = '')
        elif row == i and col == j:
            print('*', end='')
            i = i + 1
            j = j - 1
        else:
            print(end=' ')
    print()