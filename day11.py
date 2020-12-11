import numpy as np

def newseats(seats):
    old = seats.copy()
    new = seats.copy()
    changes = 0

    for i in range(len(old)):
        for j in range(len(old[0])):
            s = old[i][j]
            adjacent = 0
            a = max([i-1, 0])
            b = min([i+2, len(old)])
            c = max([j-1, 0])
            d = min([j+2, len(old[0])])

            # sum(sum((old[a:b][c:d] == '#')))

            for k in range(max([i-1, 0]), min([i+2, len(old)])):
                for l in range(max([j-1, 0]), min([j+2, len(old[0])])):
                    if old[k][l] == '#' and not (k == i and l == j): adjacent += 1

            # print('i=%d, j=%d, ad=%d' % (i, j, adjacent))
            # print('a=%d, b=%d, c=%d, d=%d' % (a, b, c, d))

            if s == 'L' and adjacent == 0:
                new[i][j] = '#'
                changes += 1
            elif s == '#' and adjacent >= 4:
                new[i][j] = 'L'
                changes += 1

    return new, changes


with open("day11input.txt", "r") as f:
    seats = f.read().strip().split("\n")

    for i in range(len(seats)):
        lst = []
        lst[:0] = seats[i]
        seats[i] = lst

    seats = np.array(seats)
    old = seats.copy()

    i = 0
    done = False
    while not done:
        new, c = newseats(old)
        if c == 0:
            done = True
        i += 1
        old = new

    s = 0
    for i in range(len(old)):
        for j in range(len(old[0])):
            if old[i][j] == '#':
                s += 1
    print(s)
