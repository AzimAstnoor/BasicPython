try:
    num = int(input('Enter the number'))
    sum = 0
    while True:
        r = num % 10
        num = num // 10
        sum = sum + r
        if num < 10:
            sum = sum + num
            break
            print('The sum of digit of number', sum)
except Exception as e: print(e)
