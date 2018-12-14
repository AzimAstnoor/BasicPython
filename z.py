i = 0
j = 5
for row in range(7):
    for col in range(6):
        if (row == 5 and col>0) or (row == 0 and col<5):
            print('*', end=' ')
        elif (row == i and col == j) :
            print('*', end=' ')
            i = i + 1
            j = j - 1
        else:
            print(end='  ')
    print()