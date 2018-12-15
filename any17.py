try:
    a = float(input('Enter the Number of Class Held:'))
    b = float(input('Enter the Number of Class Attended by Students:'))
    c = (b /a) * 100
    d = input('Any Medical Leave')
    print('Attendance of the Student is', c)
    if c >= 75:
        print('You are Allowed to sit in the Exam')
    else:
        if d == 'Y':
            print('You are Allowed due to Medical Absence')
        else:
            print('Sorry, You are Not Allowed to sit in the Exam')
except Exception as e: print(e)