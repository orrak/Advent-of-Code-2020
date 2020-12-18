import re

def evaluate1(exp):
    groups = re.findall(r'\([\*\+\s0-9]+\)', exp)
    if len(groups) > 0:
        for group in groups:
            result = evaluate1(re.sub(r'\(|\)', '', group))
            group = re.sub(r'\+', '\\\+', group)
            group = re.sub(r'\*', '\\\*', group)
            group = re.sub(r'\(', '\\\(', group)
            group = re.sub(r'\)', '\\\)', group)
            exp= re.sub(group, str(result), exp)
        return evaluate1(exp)
    else:
        nums = re.findall(r'[0-9]+', exp)
        ops = re.findall(r'\+|\*', exp)

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

def partone(data):
    s = 0
    for line in data:
        s += evaluate1(line)
    print('part one: %d' % s)

def evaluate2(exp):
    groups = re.findall(r'\([\*\+\s0-9]+\)', exp)
    if len(groups) > 0:
        for group in groups:
            result = evaluate2(re.sub(r'\(|\)', '', group))
            group = re.sub(r'\+', '\\\+', group)
            group = re.sub(r'\*', '\\\*', group)
            group = re.sub(r'\(', '\\\(', group)
            group = re.sub(r'\)', '\\\)', group)
            exp= re.sub(group, str(result), exp)
        return evaluate2(exp)
    else:
        nums = re.findall(r'[0-9]+', exp)
        ops = re.findall(r'\+|\*', exp)

        i = 0
        # do plus first
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
            val *= int(nums[i])
            i += 1

        return val

def parttwo(data):
    s = 0
    for line in data:
        s += evaluate2(line)
    print('part two: %d' % s)

with open("day18input.txt", "r") as f:
    data = f.read().strip().split("\n")
    partone(data)
    parttwo(data)
