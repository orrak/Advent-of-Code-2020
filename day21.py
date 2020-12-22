import re
import numpy as np

with open("day21input.txt", "r") as f:
    data = f.read().strip().split("\n")
    d = {}
    allallergens = []
    allings = []
    for line in data:
        line = line.split('(contains')
        foods = line[0].strip().split(' ')
        allergens = line[1].strip(')').strip(' ').split(', ')
        d[tuple(foods)] = allergens
        for ing in foods:
            if ing not in allings:
                allings.append(ing)
        for allergen in allergens:
            if allergen not in allallergens:
                allallergens.append(allergen)

    # look at lines that contain the same allergens, and see which ingredients they share

    poss = {}
    for allergen in allallergens:
        # find all lines with this allergen
        lst = [k for k in d.keys() if allergen in d[k]]
        for ing in lst[0]:
            if np.all([ing in l for l in lst]):
                # this ingredient could have this allergen
                if ing not in poss.keys():
                    poss[ing] = []
                poss[ing].append(allergen)


    # find ingredient with only one possible allergen and remove this allergen from
    # the list of possible allergens for other ingredients
    while not np.all([len(poss[k]) == 1 for k in poss.keys()]):
        for k in poss.keys():
            if len(poss[k]) == 1:
                for kk in poss.keys():
                    if k != kk and poss[k][0] in poss[kk]:
                        poss[kk].remove(poss[k][0])

    # count number of apperances of all ingredients
    count = {}
    for ing in allings:
        c = 0
        for k in d.keys():
            if ing in k:
                c += 1
        count[ing] = c

    # number of apperances of ingredients with no allergen
    print('part one: %d' % sum([count[k] for k in count.keys() if k not in poss.keys()]))

    # sort allergenic ingredients alphabetically by allergen and make comma seperated string
    lst = sorted(poss.items(), key = lambda kv:(kv[1], kv[0]))
    s = ''
    for l in lst:
        s += l[0] + ','
    print('part two: %s' % s[:-1])
