for row in range(7):
    for col in range(5):
        if row == 3 or col == 0 or col == 4:
            print('H', end=' ')
        else:
            print(end='  ')
    print()