MAX_DIAL_VALUE = 99

def dial(value):
    
    reset_value = MAX_DIAL_VALUE + 1
    if value < 0:
        mult = -value // reset_value
        remaining = value + mult * reset_value
        print(f'dial(): {value}, {(reset_value + remaining) % reset_value}')
        return (reset_value + remaining) % reset_value
    if value > MAX_DIAL_VALUE:
        mult = value // reset_value
        remaining = value - mult * reset_value
        print(f'dial(): {value}, {remaining % reset_value}')
        return remaining % reset_value
        
    print(f'dial(): {value}, {value}')
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
    print(f'initial value = {value}')
    for r in rotation_list:
        print()
        direction, distance = parse(r)
        print(direction, distance)
        value = rotation(value, direction, distance)
        if value == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    print(read_rotations('input.txt'))