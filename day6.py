def get_uniq(chunk):
    answers = []
    for line in chunk.split('\n'):
        for char in line.strip('\n'):
            if not char in answers:
                answers.append(char)
    return answers

def get_all(*chunks):
    intersection = set(chunks[0])
    for i in range(1, len(chunks)):
        intersection = intersection & set(chunks[i])
    return intersection


with open('input/day6.txt') as f:
    any_count = 0
    every_count = 0
    data = f.read()
    for chunk in data.split('\n\n'):
        any_count += len(get_uniq(chunk))
        every_count += len(get_all(*chunk.split('\n')))

    print('Part 1: {}'.format(any_count))
    print('Part 2: {}'.format(every_count))