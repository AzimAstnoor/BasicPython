n = 8
k = (2*n)-1
num = 0
for i in range(0, n):
    for j in range(0, k):
        print(end=' ')
    k = k - 1
    for j in range (0, i-1):
       print(num, end=' ')
    num = num +1
    print()