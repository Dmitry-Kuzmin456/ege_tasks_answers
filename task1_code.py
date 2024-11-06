print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = int(((x or y) and (w <= x) and (z <= w) and (not(x == y))))
                if f == 1:
                    print(x, y, z, w, '   ', f)
