def playgame(nums, stop):
    ids = {}
    i = 0
    for e in nums:
        if e in ids.keys():
            ids[e].append(i)
        else:
            ids[e] = [i]
        i += 1

    lastnum = nums[-1]
    while i < stop:
        n = lastnum
        if len(ids[n]) == 1:
            if 0 not in ids.keys():
                ids[0] = [i]
            else:
                ids[0].append(i)
            lastnum = 0
        else:
            t = ids[n][-1] - ids[n][-2]
            if t not in ids.keys():
                ids[t] = [i]
            else:
                ids[t].append(i)
            lastnum = t
        i += 1
    return lastnum

if __name__ == '__main__':
    test = [0, 3, 6]
    mine = [8,13,1,0,18,9]
    stop = 2020
    stop2 = 30000000

    print('test, 2020, %d' % playgame(test, stop))
    print('mine, 2020, %d' % playgame(mine, stop))
    print('test, 30000000, %d' % playgame(test, stop2))
    print('mine, 30000000, %d' % playgame(mine, stop2))
