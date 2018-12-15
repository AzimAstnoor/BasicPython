try:

    print(b)
    print(c)
    print(d)
    s = True
    for i in range(0,3):
      for j in range(0,3):
        if a[i][j]!=a[j][i]:
          s = False
    print(s)

except Exception as e: print(e)