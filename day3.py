with open("day3input.txt", "r") as f:
    rows = [line.strip() for line in f]
    l = len(rows[0])
    lst = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    p = 1
    for slope in lst:
        x, y = 0, 0
        r, d = slope
        trees = 0
        while x < len(rows):
            if rows[x][y] == "#":
                trees += 1
            x += d
            y += r
            if y >= l:
                y = y - l

        p = p * trees

    print(p)
