try:
    run1 = input('Enter the letter')
    run2 = input('Enter the letter')
    run3 = input('Enter the letter')
    run4 = run1 + run2 + run3
    run5 = run4 * 5
    print(run4)
    print(run5)
    count = 0
    char = input('Enter the character')
    for letter in run5:
        if (letter == char):
            count = count + 1
    print(count)
    le = list(enumerate(run4))
    ls = len(run4)
    print(le)
    print(ls)
    print('''He said, "What's this?"''')
    print('He said, "What\'s this?"')
    print("He said, \"What's this?\"")
    print("\'H\ae said, \"Wha\\t's this?\"")
    print("C:\\Python32\\Lib")
    print("This is printed\nin two lines")
    print("This is \x18\x45\x58 representation")
except Exception as e: print(e)