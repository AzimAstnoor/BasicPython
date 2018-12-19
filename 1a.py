try:
    import random

    n = random.randint(1, 9)
    g = 0
    c = 0
    while g != n and g != "exit":
        g = input("What's your guess?")
        if g == "exit":
            break
        g = int(g)
        c += 1
        if g < n:
            print("Too low!")
        elif g > n:
            print("Too high!")
        else:
            print("You got it!")
            print("And it only took you", c, "tries!")
except Exception as Z: print(Z)