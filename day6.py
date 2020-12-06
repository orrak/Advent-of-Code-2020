with open("day6input.txt", "r") as f:
    txt = f.read()
    txt = txt.split("\n\n")
    sumcount = 0
    allcount = 0
    c = 0
    for group in txt:
        people = group.strip().replace("\n", "")
        lst = []
        lst[:0] = people
        sumcount += len(list(set(lst)))

        people = group.strip().split("\n")

        lists = []
        for person in people:
            lst = []
            lst[:0] = person
            lists.append(list(set(lst)))

        intersection = lists[0]
        for i in range(len(lists)):
            intersection = list(set(intersection).intersection(lists[i]))

        allcount += len(intersection)


    print('part one', sumcount)
    print('part two', allcount)
