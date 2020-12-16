import re
import numpy as np

with open("day16input.txt", "r") as f:
    data = f.read().strip().split("\n\n")
    rules = data[0].split("\n")
    mine = [int(e) for e in data[1].split("\n")[1].split(',')]
    other = data[2].split("\n")

    ranges = []
    for rule in rules:
        lst = re.findall(r'[0-9]+', rule)
        ranges.append([int(lst[0]), int(lst[1])])
        ranges.append([int(lst[2]), int(lst[3])])

    valid = []
    invalidvalues = []
    for t in other[1:]:
        t = [int(e) for e in re.split(',', t)]
        v = True
        for num in t:
            if not np.any(np.array([num in range(r[0], r[1]+1) for r in ranges])):
                v = False
                invalidvalues.append(num)
                break
        if v:
            valid.append(t)

    print('part one: %d' % sum(invalidvalues))

    allposs = {}
    for i in range(len(mine)):
        lst = [t[i] for t in valid]

        poss = []
        for j in range(0, len(ranges)-1, 2):
            a = ranges[j]
            b = ranges[j+1]
            if np.all([(num in range(a[0], a[1]+1)) or (num in range(b[0], b[1]+1)) for num in lst]):
                poss.append(j)

        allposs[i] = poss

    while not np.all([len(allposs[k]) == 1 for k in allposs.keys()]):
        for k in allposs.keys():
            if len(allposs[k]) == 1:
                n = allposs[k][0]
                for k2 in allposs.keys():
                    if n in allposs[k2] and len(allposs[k2]) > 1:
                        allposs[k2].remove(n)

    m = 1
    for k in allposs.keys():
        i = allposs[k][0]//2
        if 'departure' in rules[i]:
            m *= mine[k]

    print('part two: %d' % m)
