try:
    def change_char(str1):
        char = str1[0]
        str1 = str1.replace(char, '$')
        str1 = char + str1[1:]
        return str1
    q = input('Enter the String to be converted')
    print(change_char(q))
except Exception as z: print(z)