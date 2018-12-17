try:
    def remove(string, n):
        first = string[:n]
        last = string[n + 1:]
        return first + last
    a = input('Enter the String')
    b = int(input("Enter the index of Charactr to remove:"))
    print(remove(a, b))
except Exception as z: print(z)