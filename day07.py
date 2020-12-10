import re

def searchbags(bags, lst, color):
    new = False
    for key in bags:
        if color in bags[key] and key not in lst:
            lst.append(key)
            new = True

    if new:
        for bag in lst:
            lst = searchbags(bags, lst, bag)
    else:
        return lst

    return lst

def countbags(bags, count, color):
    bagcount = 0 # number of bags in this bag (only the recursive bags)
    bagcountdirect = 0 # number of bags in this bag (not counting recursive bags)
    if color in bags.keys() and 'no other' not in bags[color]: # current bag contains bags
        for bag in bags[color]:
            bagcolor = re.sub(r'[0-9]+', '', bag).strip()
            numberofthisbag = int(re.match(r'^[0-9]+', bag).group(0))
            numberofbagsinside = countbags(bags, count, bagcolor)
            if numberofbagsinside > 0:
                bagcount += numberofthisbag*numberofbagsinside
            bagcountdirect += numberofthisbag
        count += bagcount+bagcountdirect
        return count
    else: # current bag in empty
        return 0


with open("day7input.txt", "r") as f:
    data = f.read().strip().split("\n")
    bags = {}
    for rule in data:
        rule = re.sub(r'\bbags?\b|\.|[0-9]+', '', rule)
        outside, inside = re.split(r'\bcontain\b', rule)
        inside = [elem.strip() for elem in inside.split(",")]

        outside = outside.strip()
        bags[outside] = inside


    lst = searchbags(bags, [], 'shiny gold')
    print('part one: %d' % len(lst))

with open("day7input.txt", "r") as f:
    data = f.read().strip().split("\n")
    bags = {}
    for rule in data:
        rule = re.sub(r'\bbags?\b|\.', '', rule)
        outside, inside = re.split(r'\bcontain\b', rule)
        inside = [elem.strip() for elem in inside.split(",")]

        outside = outside.strip()
        bags[outside] = inside
    
    count = countbags(bags, 0, 'shiny gold')
    print('part two: %d' % count)
