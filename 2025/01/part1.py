MAX_DIAL_VALUE = 99

def dial(value):
    reset_value = MAX_DIAL_VALUE + 1
    if value < 0:
        return reset_value + value
    if value > MAX_DIAL_VALUE:
        return value % reset_value
    return value
    
def rotation(value, direction, distance):
    if direction == 'L':
        return dial(value - distance)
    if direction == 'R':
        return dial(value + distance)

def parse(line):
    direction = str(line[0])
    distance = int(line[1:])
    return direction, distance

def read_rotations(txt):
    counter = 0
    with open(txt,'r') as f:
        rotation_list = f.read().split('\n')
    value = 50
    for r in rotation_list:
        direction, distance = parse(r)
        value = rotation(value, direction, distance)
        if value == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    print(read_rotations('test.txt'))