with open("day10input.txt", "r") as f:
    adapters = [int(elem) for elem in f.read().strip().split("\n")]
    builtin = max(adapters)+3
    adapters.append(builtin)

    jolts = 0
    diff1 = 0
    diff3 = 0

    lst = []

    while len(adapters) > 0:
        if jolts+1 in adapters:
            lst.append(jolts+1)
            adapters.remove(jolts+1)
            jolts += 1
            diff1 += 1
        elif jolts+2 in adapters:
            lst.append(jolts+2)
            adapters.remove(jolts+2)
            jolts += 2
        elif jolts+3 in adapters:
            lst.append(jolts+3)
            adapters.remove(jolts+3)
            jolts += 3
            diff3 += 1

    print('part one: %d' % (diff1*diff3))

    lst.append(0)
    lst.sort()

    # find elements that can be removed
    removeable = []
    for i in range(len(lst)-2):
        if lst[i+2]-lst[i] <= 3:
            removeable.append(lst[i+1])

    # make list with removable elements removed
    lstcp = lst.copy()
    for elem in removeable:
        lstcp.remove(elem)

    # find problem areas,
    # i.e, groups of consecutive elements that can not all be removed at the same time
    c = 0
    troublelst = []
    for i in range(len(lstcp)-1):
        if lstcp[i+1]-lstcp[i] > 3:
            a = lst.index(lstcp[i])
            b = lst.index(lstcp[i+1])
            troublelst.append((lstcp[i], lstcp[i+1]))
            c += 1

            for elem in lst[a:b+1]:
                if elem in removeable:
                    removeable.remove(elem)

    # all the problem areas for my input consist of three consecutive numbers
    # where any two of them can be removed, but not all three at the same time.
    # this means there are 7 options instead of 8 for each of the c groups,
    # since the empty set is not an option.
    # for all other removables we have 2 options
    print('part two: %d' % (2**len(removeable)*7**c))

    # if there were such groups of other lengths we get (2**n)-1 options for a group of length n

    # general: (2**independent_removables)*((2**n1)-1)*...*((2**nk)-1),
    # where n1...nk are lengths of removable groups
