import collections
import math
import re

containedin = collections.defaultdict(set)
contains = collections.defaultdict(list)

with open('input/day7.txt') as f:
    lines = [line.rstrip('\n') for line in f]

    for line in lines:
        color = re.match(r'(.+?) bags contain', line)[1]
        for ct, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            ct = int(ct)
            containedin[innercolor].add(color)
            contains[color].append((ct, innercolor))

    holdsgold = set()
    def count(color):
        for c in containedin[color]:
            holdsgold.add(c)
            count(c)

    count('shiny gold')

    print('Part 1: {}'.format(len(holdsgold)))

    def find_cost(color):
        total = 0
        for ct, inner in contains[color]:
            total += ct
            total += ct * find_cost(inner)
        return total
    print('Part 2: {}'.format(find_cost('shiny gold')))
