try:
    def add_string(str1):
        length = len(str1)
        if length > 2:
            if str1[-3:] == 'ing':
                str1 += 'ly'
            else:
                str1 += 'ing'
        return str1
    a = input('Enter the String to be converted')
    b = input('Enter the String to be converted')
    c = input('Enter the String to be converted')
    print(add_string(a))
    print(add_string(b))
    print(add_string(c))
except  Exception as z: print(z)