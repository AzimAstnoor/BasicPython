try:
    a = int(input("Enter the Lower Range"))
    b = int(input("Enter the Upper Range"))
    n = []
    p = int(input("Enter the First Multiple"))
    q = int(input("Enter the Second Multiple"))
    for x in range(a, b+1):
        if (x % q == 0) and (x % p == 0):
            n.append(str(x))
    print(', '.join(n))
except Exception as Z: print(Z)