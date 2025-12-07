MAX_DIAL_VALUE = 99
COUNTER = 0

def dial(value, initial_value):
    global COUNTER
    reset_value = MAX_DIAL_VALUE + 1

    if value < 0:
        mult = -value // reset_value
        remaining = value + mult * reset_value

        # print(mult)
        COUNTER += mult
        if initial_value > 0:
            COUNTER += 1

        final_value = (reset_value + remaining) % reset_value
        if final_value == 0:
            COUNTER -= 1
        print(f'dial(): {value}, {final_value}, {COUNTER}')
        return final_value
    if value > MAX_DIAL_VALUE:
        mult = value // reset_value
        remaining = value - mult * reset_value

        # print(mult)
        COUNTER += mult
        final_value = remaining % reset_value
        if final_value == 0:
            COUNTER -= 1
        print(f'dial(): {value}, {final_value}, {COUNTER}')
        return final_value
    
    print(f'dial(): {value}, {value}, {COUNTER}')
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
    print(f'initial value = {value}')
    for r in rotation_list:
        print()
        direction, distance = parse(r)
        print(value, direction, distance)
        value = rotation(value, direction, distance)
        if value == 0:
            COUNTER += 1
            print(f'pointed, {COUNTER}')
    return COUNTER

if __name__ == '__main__':
    print(read_rotations('example.txt'))