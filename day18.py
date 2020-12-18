import re

def evaluate(exp, plusfirst):
    groups = re.findall(r'\([\*\+\s0-9]+\)', exp)
    if len(groups) > 0:
        for group in groups:
            result = evaluate(re.sub(r'\(|\)', '', group), plusfirst)
            group = re.sub(r'\+', '\\\+', group)
            group = re.sub(r'\*', '\\\*', group)
            group = re.sub(r'\(', '\\\(', group)
            group = re.sub(r'\)', '\\\)', group)
            exp= re.sub(group, str(result), exp)
        return evaluate(exp, plusfirst)
    else:
        nums = re.findall(r'[0-9]+', exp)
        ops = re.findall(r'\+|\*', exp)

        if plusfirst:
            # do plus first
            i = 0
            while '+' in ops:
                if ops[i] == '+':
                    res = int(nums[i]) + int(nums[i+1])
                    ops = ops[:i] + ops[i+1:]
                    nums = nums[:i+1] + nums[i+2:]
                    nums[i] = res
                else:
                    i += 1

        val = int(nums[0])
        i = 1
        for op in ops:
            if op == '+':
                val += int(nums[i])
                i += 1
            elif op == '*':
                val *= int(nums[i])
                i += 1
        return val

def addlines(data, plusfirst):
    s = 0
    for line in data:
        s += evaluate(line, plusfirst)
    return s

with open("day18input.txt", "r") as f:
    data = f.read().strip().split("\n")
    s = addlines(data, False)
    print('part one: %d' % s)
    print('correct:', s == 30753705453324)

    s = addlines(data, True)
    print('part two: %d' % s)
    print('correct:', s == 244817530095503)
