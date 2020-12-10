with open("day1input.txt", "r") as f:
    lst = [int(line) for line in f]
    for j in range(len(lst)):
        for k in range(j, len(lst)):
            if lst[j] + lst[k] == 2020:
                print(lst[j]*lst[k]) # part one

            for l in range(k, len(lst)):
                if lst[j]+lst[k]+lst[l] == 2020:
                    print(lst[j]*lst[k]*lst[l]) # part two
