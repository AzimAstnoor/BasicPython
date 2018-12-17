try:
    p = '''`,!@#$%^&*()1234567890-_=+{}[]:";<>./?|*~'''
    a = input('Enter the String')
    n = ""
    for i in a:
        if i not in p:
            n = n + i
    print(n)
except Exception as e: print(e)