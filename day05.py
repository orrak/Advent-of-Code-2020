import numpy as np
with open("day5input.txt", "r") as f:
    seats = np.zeros((128, 8))
    maxid = 0
    for line in f:
        seat = line.strip()
        # 128 rows
        low = 0
        high = 127
        for i in range(7):
            if seat[i] == 'F':
                high = low + (high-low+1)/2. - 1
            if seat[i] == 'B':
                low = high - (high-low+1)/2. + 1

        row = high

        low = 0
        high = 7
        for i in range(7, 10):
            if seat[i] == 'L':
                high = low + (high-low+1)/2. - 1
            if seat[i] == 'R':
                low = high - (high-low+1)/2. + 1

        column = high

        seats[int(row)][int(column)] = 1

        seatid = (row * 8) + column
        if seatid > maxid:
            maxid = seatid

    for i in range(len(seats)):
        if seats[i].any() and not seats[i].all() and seats[i][0] != 0 and seats[i][-1] != 0:
            for j in range(len(seats[i])):
                if seats[i][j] == 0:
                    print("my seat ID:",i*8+j)

    print("highest seat ID:", int(maxid))
