import itertools
from pprint import pprint

sl = {}
for i in itertools.product('ABCD', repeat=3):
    sl[''.join(i)] = 0

mas = set()
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            for D in [0, 1]:
                f = (A and B) or (C and D)
                mas.add((A, B, C, D, f))

q = 0
for i in itertools.product(["<=", "and", "or", "=="], repeat=2):
    for a in itertools.product("ABCD", repeat=3):
        heraks = set()
        for A in [0, 1]:
            for B in [0, 1]:
                for C in [0, 1]:
                    for D in [0, 1]:
                        za = f'((not A or B) and (C == D)) or ((A and not C) <= (({a[0]} {i[0]} {a[1]}) {i[1]} {a[2]}))'
                        heraks.add((A, B, C, D, eval(za)))

        if len(heraks & mas) == 7:
            q += 1
            sl[''.join(a)] += 1

        if mas == heraks:
            print(*i, *a)

print(q)
print(sl)
mmax = 0
rez = ''
for key in sl:
    if sl[key] > mmax:
        mmax = sl[key]
        rez = key

print(rez)