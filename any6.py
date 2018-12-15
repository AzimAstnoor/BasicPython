try:
  a = int(input('Write the Number you want find the prime factor '))
  i = 2
  while i <= a:
    j = 2
    c = 0
    while j <= i:
      if i % j == 0:
        c = c + 1
      j = j + 1
    if c <= 1 and a % i == 0:
      print(i)
    i = i + 1
except Exception as e: print(e)