try:
    salary = float(input('Enter your Salary'))
    yos = float(input('Enter your years of service'))
    if yos > 5:
        print("Bonus is", .05 * salary)
    else:
        print("No bonus")
except Exception as e: print(e)