def part1(ranges, ids):
    fresh = 0
    for id in ids:
        for id_range in ranges:
            if id_range[0] <= id <= id_range[1]:
                fresh += 1
                break
    return fresh

def part2():
    # current_range: current_min, current_max
    # for each new range:
    # new_range: new_min, new_max
    #   check every existing range
    #       case 1:  new_min in between current_min and current_max
    #       case 2:  new_max in between current_min and current_max
    #       case 3:  current_range INSIDE new_range
    #       case 4:  new_range INSIDE current_range
    #       case 5:  new_range OUTSIDE current_range
    pass


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
    split_ix = lines.index('')
    ranges = [a.split('-') for a in lines[:split_ix]]
    ranges = [[int(a), int(b)] for a,b in ranges]
    ids = [int(id) for id in lines[split_ix+1:]]
    # print(ranges)
    # print(ids)
    print(part1(ranges, ids))