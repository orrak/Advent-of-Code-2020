import re

def run(instructions):
    acc = 0
    pos = 0
    done = False
    while(not done):
        if pos != len(instructions):
            instruction = instructions[pos]
            number = int((re.search(r'-?[0-9]+', instruction)).group(0))
            if 'done' in instruction:
                done = True
            else:
                instructions[pos] += ', done'
                if 'acc' in instruction:
                    acc += number
                    pos += 1
                elif 'jmp' in instruction:
                    pos += number
                elif 'nop' in instruction:
                    pos += 1
        else:
            done = True

    return acc, pos

with open("day8input.txt", "r") as f:
    instructions = f.read().strip().split("\n")
    acc, pos = run(instructions.copy())
    print('part one: %d' % acc)

    for i in range(len(instructions)):
        instrcp = instructions.copy()
        # print(instrcp[i])
        if 'jmp' in instrcp[i]:
            instrcp[i] = re.sub('jmp', 'nop', instrcp[i])
            acc, pos = run(instrcp)
            if pos == len(instrcp):
                print('part two: %d' % acc)
            instrcp[i] = re.sub('nop', 'jmp', instrcp[i])

        elif 'nop' in instrcp[i]:
            instrcp[i] = re.sub('nop', 'jmp', instrcp[i])
            acc, pos = run(instrcp)
            if pos == len(instrcp):
                print('part two: %d' % acc)
            instrcp[i] = re.sub('jmp', 'nop', instrcp[i])
