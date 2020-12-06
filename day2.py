from operator import xor

def is_valid_password(line):
    pt1, pt2, pt3 = line.split(' ')
    n_min, n_max = pt1.split('-')
    char_count = count_chars(pt3, pt2[0])

    if char_count > int(n_max) or char_count < int(n_min):
        return False
    return True

def is_valid_password_corrected(line):
    pt1, pt2, pt3 = line.split(' ')
    index1, index2 = pt1.split('-')
    char = pt2[0]
    pt3 = pt3.strip('\n')

    return xor(pt3[int(index1) - 1] == char, pt3[int(index2) - 1] == char)

def count_chars(text, char):
    counter = 0
    for c in text:
        if c == char:
            counter += 1
    return counter

valid_passwords = 0
valid_corrected_passwords = 0
with open('input/day2.txt') as f:
    for line in f:
        if is_valid_password(line):
            valid_passwords += 1
        if is_valid_password_corrected(line):
            valid_corrected_passwords += 1

    print('Part 1: {}'.format(valid_passwords))
    print('Part 2: {}'.format(valid_corrected_passwords))

