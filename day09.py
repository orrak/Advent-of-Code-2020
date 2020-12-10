with open("day9input.txt", "r") as f:
    nums = [int(num) for num in f.read().strip().split("\n")]
    start = 0
    while start < len(nums)-26:
        lst = nums[start:start+25]
        check = nums[start+25]
        found = False
        for i in lst:
            for j in lst:
                if i != j and i+j == check:
                    found = True
        if not found:
            break
        start += 1

    print('part one: %d' % check)

    start = 0
    end = 0
    while not found:
        s = sum(nums[start:end])
        if s < check:
            end += 1
        elif s > check:
            start += 1
        else:
            break

    print('part two: %d' % (min(nums[start:end])+max(nums[start:end])))
