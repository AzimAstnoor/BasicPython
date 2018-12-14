Sc = float(input('Enter Science marks:'))
st = (Sc/100)*100
Mt = float(input('Enter Maths marks:'))
mt = (Mt/100)*100
En = float(input('Enter English marks:'))
et = (En/100)*100
Ss = float(input('Enter Social marks:'))
St = (Ss/100)*100
Hi = float(input('Enter Hindi marks:'))
ht = (Hi/100)*100
Total = ((Sc + Mt + En + Ss + Hi)/500)*100
if Total in range(91,101):
    if Total>95 and Total<101:
        print('Congrats, You got A+ Grade')
    elif Total == 100:
        print('You are a Topper')
    else:
        print('Congrats, You got A- Grade')
if Total in range(81,91):
    if Total > 85 and Total < 91:
        print('Well Done, You got B+ Grade')
    else:
        print('Well Done, You got B- Grade')
if Total in range(71, 81):
    if Total > 75 and Total < 81:
        print('Very Good, You got C+ Grade')
    else:
        print('Very Good, You got C- Grade')
if Total in range(61,71):
    if Total > 65 and Total < 71:
        print('Work Hard, You got D+ Grade')
    else:
        print('Work Hard, You got D- Grade')
if Total in range(51,61):
    if Total > 55 and Total < 61:
        print('Need to Work Really Hard, You got E+ Grade')
    else:
        print('Need to Work Really Hard, You got E- Grade')
if Total in range(51):
    print(' You are staying with me another year.')
print('Your Grade in Science is',st)
print('Your Grade in Math is',mt)
print('Yor Grade in English',et)
print('Your Grade in Social Science',St)
print('Your Grade in Hindi',ht)