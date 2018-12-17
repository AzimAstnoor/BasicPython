try:
    c = "bcdfghklmnpqrstwvyxzBCDFGHKLMNPQRSTWVYXZ"
    a = input('Enter the String')
    n = ""
    for i in a:
        if i not in c:
            n = n + i
    print(n)
except Exception as e: print(e)