import numpy as np
import math

def gettime(times, buses, start, stop):
    done = False
    t = start
    while not done:
        if not np.any((t+times)%buses):
            done = True
        if t == stop:
            return None
        t += 1
    return t-1


with open("day13input.txt", "r") as f:
    data = f.read().split("\n")
    earliest = int(data[0])
    busesx = data[1].split(',')

    buses = np.array([int(b) for b in busesx if b != 'x'])
    lst = [earliest//b for b in buses]

    earliestbuses = []

    for i in range(len(buses)):
        time = buses[i]*lst[i]
        while time < earliest:
            time += buses[i]
        earliestbuses.append(time)

    first = min(earliestbuses)
    ID = buses[earliestbuses.index(first)]
    wait = min(earliestbuses)-earliest
    print('part one: %d' % (ID*wait))

    times = np.array([i for i in range(len(busesx)) if busesx[i] != 'x'])

    s = ''
    for i in range(len(times)):
        s += ('(t+%d)%s%d=0, ' % (times[i], '%', buses[i]))
    print('part two: %s' % (s[:-1]))

    # input s into wolframalpha
    # answer: 741745043105674 + 1182259336403743 n
