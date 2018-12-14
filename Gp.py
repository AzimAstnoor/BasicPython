a = float(input('Enter the first no. of geometric progression'))
b = float(input('Enter the ratio'))
c = float(input('Enter the no. terms you want'))
d = 0
while d <= c:
    e = a * (b ** d)
    print(e)
    d = d + 1
