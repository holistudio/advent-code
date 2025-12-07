MAX_DIAL_VALUE = 99
COUNTER = 0

def dial(value, initial_value):
    global COUNTER
    reset_value = MAX_DIAL_VALUE + 1
    if value < 0:
        mult = -value // reset_value
        remaining = value + mult * reset_value
        COUNTER += mult
        if initial_value > 0:
            COUNTER += 1
        final_value = (reset_value + remaining) % reset_value
        if final_value == 0:
            COUNTER -= 1
        return final_value
    if value > MAX_DIAL_VALUE:
        mult = value // reset_value
        remaining = value - mult * reset_value
        COUNTER += mult
        final_value = remaining % reset_value
        if final_value == 0:
            COUNTER -= 1
        return final_value
    return value
    
def rotation(value, direction, distance):
    if direction == 'L':
        return dial(value - distance, value)
    if direction == 'R':
        return dial(value + distance, value)

def parse(line):
    direction = str(line[0])
    distance = int(line[1:])
    return direction, distance

def read_rotations(txt):
    global COUNTER
    with open(txt,'r') as f:
        rotation_list = f.read().split('\n')
    value = 50
    for r in rotation_list:
        direction, distance = parse(r)
        value = rotation(value, direction, distance)
        if value == 0:
            COUNTER += 1
    return COUNTER

if __name__ == '__main__':
    print(read_rotations('input.txt'))