a = int(input('Enter the Lower range of Armstrong No.:'))
b = int(input('Enter the Upper range of Armstrong No.:'))
while a < b:
     c = a//10
     d = c - ((a//100)*10)
     e = a//100
     f = a - (e * 100) -(d * 10)
     g = (e**3) + (d**3) + (f**3)
     if g == a:
        print(g,' is a Armstrong Number')
     a = a + 1


