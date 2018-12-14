j = 8
i = 0
for row in range(14):
    for col in range(14):
     if row == 0 and col<7 and col>1:
        print('*', end=' ')
     elif row == i and col == j and col>1:
            print('*', end='')
            i = i+1
            j = j-1
     else:
        print(end='  ')
    print()