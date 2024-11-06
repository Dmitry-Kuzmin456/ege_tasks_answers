from itertools import *

a = []
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                for q in [0, 1]:
                    f1 = not ((x and not y) or (not z and w and q) or (x and y and not w))
                    if f1 == 1:
                        a.append(tuple([x, y, z, w, q]))
b = []
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                for q in [0, 1]:
                    f2 = ((x or y or not z) and ((w and not q) or (z and y)))
                    if f2 == 1:
                        b.append(tuple([x, y, z, w, q]))

set_a = set(a)
set_b = set(b)
print(*a, sep='\n')
print()
print(*b, sep='\n')
print()
mas = list(set_a & set_b)


def f(x, y, z, w, q):
    return ((y and not x) or (z and w)) and (q or w or not z)


print(*sorted(mas), sep='\n')
for p in permutations('xyzwq'):
    if [f(**dict(zip(p, r))) for r in mas] == [1] * len(mas):
        print(p)
