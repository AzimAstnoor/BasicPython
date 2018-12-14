print('Writ no. number you want to compare\n'
      '2\n'
      '3\n'
      '4\n')
p = float(input('Choose'))
if p == 2:
    a = float(input('NumberA'))
    b = float(input('NumberB'))
    if a > b:
        print('A is the Maximum Number and B is the Minimum Number')
    if a < b:
        print('B is the Maximum Number and A is the Minimum Number')
if p == 3:
    a = float(input('NumberA'))
    b = float(input('NumberB'))
    c = float(input('NumberC'))
    if a > b:
        if a > c:
            print('A is the Maximum Number')
            if b > c:
                print('C is the Minimum Number')
            if b < c:
                print('B is the Minimum Number')
        if c > a:
            print('C is the Maximum Number')
            print('B is the Minimum Number')
    if a < b:
        if b > c:
            print('B is the Maximum Number')
            if a > c:
                print('A is the Minimum Number')
            if a < c:
                print('C is the Minimum Number')
        if c > b:
            print('C is the Maximum Number')
            print('A is the Minimum Number')
if p == 4:
    a = float(input('NumberA'))
    b = float(input('NumberB'))
    c = float(input('NumberC'))
    d = float(input('NumberD'))
    if a > b:
        if a > c:
            if a > d:
                print('A is the Maximum Number')
                if d > c:
                    if c > b:
                        print('B is the Minimum Number')
                    if c < b:
                        print('C is the Minimum Number')
                if d < c:
                    if d < b:
                        print('D is the Minimum Number')
                    if d > b:
                        print('B is the Minimum Number')
            if d < a:
                print('A is the Minimum Number')
                if c > b:
                    print('B is the Minimum Number')
                if c < b:
                    print('C is the Minimum Number')
        if c > a:
            if c > d:
                print('C is the Maximum Number')
                if d > a:
                    if a > b:
                        print('B is the Minimum Number')
                    if a < b:
                        print('A is the Minimum Number')
                if d < a:
                    if d < b:
                        print('D is the Minimum Number')
                    if d > b:
                        print('B is the Minimum Number')
            if d < a:
                print('D is the Maximum Number')
                if c > b:
                    print('B is the Minimum Number')
                if c < b:
                    print('C is the Minimum Number')
    if b > a:
        if b > c:
            if b > d:
                print('B is the Maximum Number')
                if d > c:
                    if c > a:
                        print('A is the Minimum Number')
                    if c < a:
                        print('C is the Minimum Number')
                if d < c:
                    if d < a:
                        print('D is the Minimum Number')
                    if d > a:
                        print('A is the Minimum Number')
            if d < b:
                print('A is the Minimum Number')
                if c > a:
                    print('B is the Minimum Number')
                if c < b:
                    print('C is the Minimum Number')
        if c > a:
            if c > d:
                print('C is the Maximum Number')
                if d > a:
                    if a > b:
                        print('B is the Minimum Number')
                    if a < b:
                        print('A is the Minimum Number')
                if d < a:
                    if d < b:
                        print('D is the Minimum Number')
                    if d > b:
                        print('B is the Minimum Number')
            if d < b:
                print('D is the Maximum Number')
                if c > a:
                    print('A is the Minimum Number')
                if c < a:
                    print('C is the Minimum Number')