import numpy as np

def adjacent1(old, i, j):
    a = max([i-1, 0])
    b = min([i+2, len(old)])
    c = max([j-1, 0])
    d = min([j+2, len(old[0])])
    return sum(sum((old[a:b, c:d] == '#')))

def adjacent2(old, i, j):
    ad = 0
    # for each 8 direction, is there a visible occupied seat?
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1],
                  [1, 1], [1, 0], [1, -1], [0, -1]]

    for direction in directions:
        vs = findvisibleseat(old, i, j, direction)
        if vs == '#':
            ad += 1

    return ad

def newseats(seat, adfunc):
    old = seats.copy()
    new = seats.copy()
    changes = 0

    for i in range(len(old)):
        for j in range(len(old[0])):
            s = old[i][j]
            adjacent = adfunc(old, i, j)

            if s == '#':
                adjacent -= 1

            if s == 'L' and adjacent == 0:
                new[i][j] = '#'
                changes += 1
            elif s == '#' and adjacent >= 4:
                new[i][j] = 'L'
                changes += 1

    return new, changes

# part one
def newseats1(seats):
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

            adjacent = sum(sum((old[a:b, c:d] == '#')))
            if s == '#':
                adjacent -= 1

            if s == 'L' and adjacent == 0:
                new[i][j] = '#'
                changes += 1
            elif s == '#' and adjacent >= 4:
                new[i][j] = 'L'
                changes += 1

    return new, changes

def findvisibleseat(seats, i, j, direction):
    pos = np.array([i, j])
    pos = pos + direction

    while 0 <= pos[0] < len(seats) and 0 <= pos[1] < len(seats[0]):
        if seats[pos[0]][pos[1]] != '.':
            return seats[pos[0]][pos[1]]
        pos = pos + direction


    if not (0 <= pos[0] < len(seats) and 0 <= pos[1] < len(seats[0])):
        return '.'

    return seats[pos[0]][pos[1]]

# part two
def newseats2(seats):
    old = seats.copy()
    new = seats.copy()
    changes = 0

    for i in range(len(old)):
        for j in range(len(old[0])):
            s = old[i][j]
            adjacent = 0

            # for each 8 direction, is there a visible occupied seat?
            directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1],
                          [1, 1], [1, 0], [1, -1], [0, -1]]

            for direction in directions:
                vs = findvisibleseat(old, i, j, direction)
                if vs == '#':
                    adjacent += 1

            if s == 'L' and adjacent == 0:
                new[i][j] = '#'
                changes += 1
            elif s == '#' and adjacent >= 5:
                new[i][j] = 'L'
                changes += 1

    return new, changes

def partone(old):
    done = False
    while not done:
        new, c = newseats(old, adjacent1)
        if c == 0:
            done = True
        old = new

    print('part one: %d' % (sum(sum((old == '#')))))

def parttwo(old):
    done = False
    oldc = 0
    i = 0
    while not done:
        new, c = newseats2(old, adjacent2)
        if c == 0:
            done = True
        if c == oldc:
            exit()
        oldc = c
        old = new
        i += 1

    print('part two: %d' % (sum(sum((old == '#')))))


if __name__ == '__main__':
    with open("day11input.txt", "r") as f:
        seats = f.read().strip().split("\n")

        for i in range(len(seats)):
            lst = []
            lst[:0] = seats[i]
            seats[i] = lst

        seats = np.array(seats)
        partone(seats.copy())
        parttwo(seats.copy())
