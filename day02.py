import re

with open("day2input.txt", "r") as f:
    passwords = [re.split(r'-|:|\s', line.strip()) for line in f]

    # part one
    s = 0
    for i in range(len(passwords)):
        m, n, l, a, pw = passwords[i]
        if int(m) <= len(re.findall(l, pw)) <= int(n):
            s += 1

    print(s)

    # part two
    s = 0
    for i in range(len(passwords)):
        m, n, l, a, pw = passwords[i]
        if (pw[int(m)-1]==l) != (pw[int(n)-1]==l):
            s += 1

    print(s)
