import re

def is_valid_hexcolor(text):
    match = re.search(r'^#(?:[0-9a-fA-F]{6})$', text)
    return bool(match)

def parse_passport(text):
    passport = {}
    for line in text.split('\n'):
        for word in line.split(' '):
            [key, value] = word.split(':')
            passport[key] = value
    return passport


def is_valid_passport(passport, extra_validation = False):
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport_keys = list(passport.keys())
    passport_items = list(passport.items())
    for field in valid_fields:
        if not field in passport_keys:
            return False

    if not extra_validation:
        return True

    for [key, value] in passport_items:
        if key == 'byr':
            if int(value) < 1920 or int(value) > 2002:
                return False
        elif key == 'iyr':
            if int(value) < 2010 or int(value) > 2020:
                return False
        elif key == 'eyr':
            if int(value) < 2020 or int(value) > 2030:
                return False
        elif key == 'hgt':
            if 'cm' in value:
                hgt = int(value.strip('cm'))
                if hgt < 150 or hgt > 193:
                    return False
            elif 'in' in value:
                hgt = int(value.strip('in'))
                if hgt < 59 or hgt > 76:
                    return False
            else:
                return False
        elif key == 'hcl':
            if not is_valid_hexcolor(value):
                return False
        elif key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif key == 'pid':
            if not len(value) == 9:
                return False

    return True


with open('input/day4.txt') as f:
    data = f.read()
    valid_passports = 0
    valid_passports_extra_validation = 0

    for passport_data in data.split('\n\n'):
        passport = parse_passport(passport_data)
        if is_valid_passport(passport):
            valid_passports += 1
        if is_valid_passport(passport, extra_validation=True):
            valid_passports_extra_validation += 1

    print('Part 1: {}'.format(valid_passports))
    print('Part 2: {}'.format(valid_passports_extra_validation))
