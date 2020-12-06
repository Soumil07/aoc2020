def extend(line, n_min):
    tmp = line
    while len(line) < n_min:
        line += tmp
    return line

def get_trees(lines, slope):
    (run, rise) = slope
    line_counter = 0
    index_counter = 0
    n_trees = 0

    while line_counter < len(lines) - 1:
        line_counter += rise
        index_counter += run
        line = lines[line_counter].strip('\n')
        if index_counter >= len(line):
            line = extend(line, index_counter + 1)
        if line[index_counter] == '#':
            n_trees += 1
    
    return n_trees

with open('input/day3.txt') as f:
    lines = f.readlines()
    n_trees = get_trees(lines, (3, 1))

    print('Part 1: {}'.format(n_trees))

    print('Part 2: {}'.format(get_trees(lines, (1, 1)) * n_trees * get_trees(lines, (5, 1)) * get_trees(lines, (7, 1)) * get_trees(lines, (1, 2))))


