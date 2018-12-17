try:
    quantity = float(input('Enter the quantity you want t buy:-'))
    if quantity * 100 > 1000:
        print("Cost is", ((quantity * 100) - (0.1 * quantity * 100)))
    else:
        print("Cost is", quantity * 100)
except Exception as e: print(e)