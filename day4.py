import re

with open("day4input.txt", "r") as f:
    txt = f.read()
    passports = txt.split('\n\n')
    passports = [re.split(r'\s', p.strip()) for p in passports]

    ecllst = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    valid1 = 0
    valid2 = 0
    for passport in passports:
        p = {}
        for entry in passport:
            key, val = entry.split(":")
            p[key] = val

        if ('byr' in p and
           'iyr' in p and
           'eyr' in p and
           'hgt' in p and
           'hcl' in p and
           'ecl' in p and
           'pid' in p):
               valid1 += 1
               byr = 1920 <= int(p['byr']) <= 2002
               iyr = 2010 <= int(p['iyr']) <= 2020
               eyr = 2020 <= int(p['eyr']) <= 2030
               ecl = p['ecl'] in ecllst
               hcl = re.match(r'#([0-9]|[a-f]){6}', p['hcl']) != None
               pid = re.match(r'[0-9]{9}', p['pid']) != None

               hgtunit = p['hgt'][-2:]
               hgtnum = p['hgt'][:-2]
               if len(hgtnum) > 0:
                   hgtnum = int(hgtnum)
               hgt = ((hgtunit == 'cm' and 150 <= hgtnum <= 193) or
                      (hgtunit == 'in' and 59 <= hgtnum <= 76))

               if (byr and iyr and eyr and hgt and hcl and ecl and pid):
                   valid2 += 1

    print('Valid passports (part one):', valid1)
    print('Valid passports (part two):', valid2)


# failed answers (part two): 199
