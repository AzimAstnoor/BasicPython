try:
    a = []
    b = []
    c = []
    d = []
    a1 = []
    b1 = []
    c1 = []
    d1 = []
    a2 = []
    b2 = []
    c2 = []
    d2 = []
    a3 = []
    b3 = []
    c3 = []
    d3 = []
    p = int(input('First element'))
    q = int(input('Second element'))
    r = int(input('Third element'))
    w = int(input('Fourth element'))
    e = int(input('Fifth element'))
    o = int(input('Sixth element'))
    t = int(input('Seventh element'))
    y = int(input('Eight element'))
    u = int(input('Ninth element'))
    b = [p, q, r]
    c = [w, e, o]
    d = [t, y, u]
    a = [b, c, d]
    print(a)
    p1 = int(input('First element'))
    q1 = int(input('Second element'))
    r1 = int(input('Third element'))
    w1 = int(input('Fourth element'))
    e1 = int(input('Fifth element'))
    o1 = int(input('Sixth element'))
    t1 = int(input('Seventh element'))
    y1 = int(input('Eight element'))
    u1 = int(input('Ninth element'))
    b1 = [p1, q1, r1]
    c1 = [w1, e1, o1]
    d1 = [t1, y1, u1]
    a1 = [b1, c1, d1]
    b2 = [p1+p, q1+q, r1+r]
    c2 = [w1+w, e1+e, o1+o]
    d2 = [t1+t, y1+y, u1+u]
    a2 = [b2, c2, d2]
    b3 = [p1*p, q1*q, r1]
    c3 = [w1*w, e1*e, o1*o]
    d3 = [t1*t, y1*y, u1*u]
    a3 = [b3, c3, d3]
    print(a1)
    print(a2)
    print(a3)
except Exception as e: print(e)