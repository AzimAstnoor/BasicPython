try:
    a = input('Enter the String')
    a = a.casefold()
    b = reversed(a)
    if list(a) == list(b):
        print('Yes, This String is Palindrome.')
    else:
        print('No, This String is Not Palindrome.')
except Exception as e: print(e)