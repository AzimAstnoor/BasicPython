try:
    from decimal import Decimal as D
    from fractions import Fraction as F
    import math
    import random
    a = int(input('Enter the number'))
    b = float(input('Enter th number'))
    c = complex(input('Enter the number'))
    print(a + 3)
    print(b + 3)
    print(c + 3)
    print(type(a))
    print(isinstance(a, int))
    print(isinstance(a, float))
    print(isinstance(a, complex))
    print(type(b))
    print(isinstance(b, int))
    print(isinstance(b, float))
    print(isinstance(b, complex))
    print(type(c))
    print(isinstance(c, int))
    print(isinstance(c, float))
    print(isinstance(c, complex))
    print(0B011011011101010)
    print(0B1110010101 + 0XAFB)
    print(0O15 * 0B110101)
    print(0.154)
    print(D(0.154))
    print(D(0.154) + D(0.541))
    print(D(1.54) * D(0.541))
    print(F(0.154))
    print(F(5))
    print(F(5, 6))
    print(F(0.154) + F(0.541))
    print(F(1.54) * F(0.541))
    print(math.pi)
    print(math.factorial(100))
    print(math.ceil(100))
    print(math.fabs(4.99))
    print(random.random)
    print(random.randrange(1, 100))
except Exception as e: print(e)