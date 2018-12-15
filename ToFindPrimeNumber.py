a = int(input('Enter the number Lower range'))
b = int(input('Enter the the Upper Range'))
for n in range(a,b+1):
    m = n%2
    k = n%3
    c = n/2
    d = n/3
    u = n % 5
    i = n % 7
    g = n / 5
    j = n / 7
    if (m!=0 and k != 0 and u != 0 and i !=0 )\
        or g == 1 or j == 1 or c == 1 or d == 1 :
        print(n,' is a Prime Number\n')