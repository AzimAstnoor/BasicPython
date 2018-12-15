try:
    i = 20
    a = []
    while i>0:
      num = int(input('Enter the Number'))
      a.append(num)
      i = i-1
    odd = 0
    even = 0
    zero = 0
    positive = 0
    negative = 0
    i = 19
    while i>=0:
      if a[i] == 0:
        zero = zero+1
      elif a[i]>0:
        positive = positive + 1
        if a[i]%2 == 0:
          even = even + 1
        else:
          odd = odd + 1
      else:
          negative = negative + 1
          if a[i] % 2 == 0:
              even = even + 1
          else:
              odd = odd + 1
      i = i - 1
    print('Even :', even)
    print('Odd :', odd)
    print('Zero :', zero)
    print('Positive :', positive)
    print('Negative :', negative)


except Exception as e: print(e)