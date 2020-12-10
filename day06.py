with open("day6input.txt", "r") as f:
    txt = f.read().split("\n\n")
    sumcount = 0
    allcount = 0

    for group in txt:
        sumcount += len(list(set([char for char in group.strip().replace("\n", "")])))

        people = group.strip().split("\n")
        intersection = people[0]
        for person in people:
            intersection = list(set(intersection).intersection(person))
        allcount += len(intersection)

    print('part one', sumcount)
    print('part two', allcount)
