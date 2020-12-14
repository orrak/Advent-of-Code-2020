import numpy as np

def partone(instructions):
    pos = [0, 0]
    direction = 0 # in degrees
    for instruction in instructions:
        action = instruction[0]
        value = instruction[1]

        if action == 'N':
            pos[1] += value
        elif action == 'S':
            pos[1] -= value
        elif action == 'E':
            pos[0] += value
        elif action == 'W':
            pos[0] -= value
        elif action == 'L':
            direction += value
            if direction < 0: direction = 360 + direction
            if direction > 360: direction = direction - 360
        elif action == 'R':
            direction -= value
            if direction < 0: direction = 360 + direction
            if direction > 360: direction = direction - 360
        elif action == 'F':
            if direction == 0 or direction == 360:
                pos[0] += value
            elif direction == 90:
                pos[1] += value
            elif direction == 180:
                pos[0] -= value
            elif direction == 270:
                pos[1] -= value
            else:
                print('error')
                exit()

    print('part one: %d' % (abs(pos[0])+abs(pos[1])))

def parttwo(instructions):
    pos = np.array([0, 0])
    waypoint = np.array([10, 1])

    for instruction in instructions:
        action = instruction[0]
        value = instruction[1]
        diff = waypoint-pos

        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'L':
            a = waypoint[0]
            b = waypoint[1]
            if value == 90:
                waypoint = [-b, a]
            elif value == 180:
                waypoint = [-a, -b]
            elif value == 270:
                waypoint = [b, -a]
        elif action == 'R':
            a = waypoint[0]
            b = waypoint[1]
            if value == 90:
                waypoint = [b, -a]
            elif value == 180:
                waypoint = [-a, -b]
            elif value == 270:
                waypoint = [-b, a]
        elif action == 'F':
            for i in range(value):
                pos += waypoint

    print('part two: %d' % (abs(pos[0])+abs(pos[1])))

with open("day12input.txt", "r") as f:
    instructions = [(i[0], int(i[1:])) for i in f.read().strip().split("\n")]
    partone(instructions)
    parttwo(instructions)

