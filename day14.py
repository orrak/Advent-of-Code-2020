import numpy as np
import re

def initprogram1(data):
    memory = {}
    mask = ''
    for line in data:
        if 'mask' in line:
            mask = line.split('= ')[1]
        elif 'mem' in line:
            matches = re.findall(r'[0-9]+', line)
            add = int(matches[0])
            value = str(bin(int(matches[1])))[2:]
            v = list(str(0)*(len(mask)-len(value)) + value)
            m = list(mask)
            r = list(str('A')*len(mask))
            for i in range(len(m)):
                if m[i] == 'X':
                    r[i] = v[i]
                else:
                    r[i] = m[i]
            r = ''.join(r)
            # print('value: ', value)
            # print('mask:  ', mask)
            # print('result:', result)
            memory[add] = int(r, 2)

    print('part one: %d' % sum(memory.values()))

def comb(mask):
    lst = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            mcp1 = mask.copy()
            mcp1[i] = '0'
            lst += comb(mcp1)
            mcp2 = mask.copy()
            mcp2[i] = '1'
            lst += comb(mcp2)
            break
    if 'X' not in mask:
        lst.append(mask)
    return lst


def initprogram2(data):
    memory = {}
    mask = ''
    m = []
    for line in data:
        if 'mask' in line:
            mask = line.split('= ')[1]
            m = list(mask)
        elif 'mem' in line:
            matches = re.findall(r'[0-9]+', line)

            add = str(bin(int(matches[0])))[2:]
            value = int(matches[1])

            a = list(str(0)*(len(mask)-len(add)) + add)
            r = list(str('A')*len(mask))

            for i in range(len(m)):
                if m[i] == 'X' or m[i] == '1':
                    r[i] = m[i]
                else:
                    r[i] = a[i]
            combs = comb(r)

            for c in combs:
                 na = int(''.join(c), 2)
                 # print(na)
                 memory[na] = value

    print('part two: %d' % sum(memory.values()))

if __name__ == '__main__':
    with open("day14input.txt", "r") as f:
        data = f.read().strip().split("\n")

        initprogram1(data)

        '''
        for line in data:
            if 'mask' in line:
                print(2**len(re.findall(r'X', line)))
        '''
        initprogram2(data)

# 1572948371929 too low (part two)
