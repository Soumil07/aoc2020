def interpret(lines, exception=False):
    instructions = set()

    i = 0
    acc = 0
    while True:
        if i == len(lines) and exception:
            return acc

        line = lines[i]
        int_identifier = '{}-{}'.format(i, line)
        if int_identifier in instructions:
            if exception:
                raise Exception()
            return acc

        # set the current instruction in the instruction map
        instructions.add(int_identifier)
        opcode, value = line.split(' ')

        if opcode == 'nop':
            i += 1
            continue
        elif opcode == 'acc':
            acc += int(value)
            i += 1
        elif opcode == 'jmp':
            i += int(value)

with open('input/day8.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    
    print('Part 1: {}'.format(interpret(lines)))

    for i in range(len(lines)):
        copy = lines[:]
        line = copy[i]
        instruction, value = line.split(' ')
        if instruction == 'acc':
            continue

        if instruction == 'nop':
            copy[i] = 'jmp {}'.format(value)
        elif instruction == 'jmp':
            copy[i] = 'nop {}'.format(value)

        try:
            print('Part 2: {}'.format(interpret(copy, exception=True)))
        except:
            continue
