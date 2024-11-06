import itertools

sl = {}
for i in itertools.product('xyzw', repeat=3):
    sl[''.join(i)] = 0

mas = set()
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = (x and y) or (z and w)
                mas.add((x, y, z, w, f))

for i in itertools.product(["<=", "and", "or", "=="], repeat=2):
    for a in itertools.product("xyzw", repeat=3):
        comb = set()
        for x in [0, 1]:
            for y in [0, 1]:
                for z in [0, 1]:
                    for w in [0, 1]:
                        za = f'((not x or y) and (z == w)) or ((x and not z) <= (({a[0]} {i[0]} {a[1]}) {i[1]} {a[2]}))'
                        comb.add((x, y, z, w, eval(za)))

        if len(comb & mas) == 7:
            sl[''.join(a)] += 1

print(sl)
mmax = 0
rez = ''
for key in sl:
    if sl[key] > mmax:
        mmax = sl[key]
        rez = key

print(rez)
