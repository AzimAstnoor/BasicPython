i = 0
j = 5
for row in range(14):
    for col in range(14):
     if col == 6 or (row == 13 and (col>1 and col<11)):
        print('*', end=' ')
     elif row == i and col == j and col>1:
            print('*', end=' ')
            i = i+1
            j = j-1
     else:
        print(end='  ')
    print()
