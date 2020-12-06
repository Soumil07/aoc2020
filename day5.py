def get_bounds(b_min, b_max, lower=True):
    if b_max == b_min + 1:
        return b_min if lower else b_max
    mean = (b_min + b_max + 1) / 2
    if lower:
        return (b_min, mean - 1)
    return (mean, b_max)

def parse_line(line):
    row_bounds = (0, 127)
    for i in range(7):
        row_bounds = get_bounds(*row_bounds, lower=line[i] == 'F')

    col_bounds = (0, 7)
    for i in range(7, 10):
        col_bounds = get_bounds(*col_bounds, lower=line[i] == 'L')
    return (row_bounds, col_bounds)

def get_seat_id(row, col):
    return row * 8 + col

with open('input/day5.txt') as f:
    seat_ids = []
    for line in f:
        line = line.strip('\n')
        row, col = parse_line(line)
        seat_ids.append(get_seat_id(row, col))

    print('Part 1: {}'.format(max(seat_ids)))

    for col in range(0, 7):
        for row in range(0, 127):
            seat_id = get_seat_id(row, col)
            if seat_id not in seat_ids and (seat_id + 1) in seat_ids and (seat_id - 1) in seat_ids:
                print('Part 2: {}'.format(seat_id))
