greater_than_1010 = []
smaller_than_1010 = []

with open('input/day1.txt') as f:
    for line in f:
        num = int(line)
        if num < 1010:
            smaller_than_1010.append(num)
        else:
            greater_than_1010.append(num)

for num1 in greater_than_1010:
    for num2 in smaller_than_1010:
        if num1 + num2 == 2020:
            print('Part 1: {}'.format(num1 * num2))
        else:
            if num1 + num2 < 1010:
                for num3 in greater_than_1010:
                    if num1 + num2 + num3 == 2020:
                        print('Part 2: {}'.format(num1 * num2 * num3))
            else:
                for num3 in smaller_than_1010:
                    if num1 + num2 + num3 == 2020:
                        print('Part 2: {}'.format(num1 * num2 * num3))
