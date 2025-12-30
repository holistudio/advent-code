def part1(ranges, ids):
    fresh = 0
    for id in ids:
        for id_range in ranges:
            if id_range[0] <= id <= id_range[1]:
                fresh += 1
                break
    return fresh

def part2(ranges):
    distinct_ranges = [ranges[0]]
    # for each new range:
    for new_range in ranges[1:]:
        # print(f'new_range: {new_range}')
        # print(f'BEFORE: {distinct_ranges}')
        # new_range: new_min, new_max
        new_min, new_max = new_range[0], new_range[1]

        distinct = True
        # check every existing range
        for current_range in distinct_ranges:
            # current_range: current_min, current_max
            current_min, current_max = current_range[0], current_range[1]
            #       case 1:  new_min in between current_min and current_max
            if (current_min <= new_min <= current_max) and (new_max >= current_max):
                current_range[1] = new_max
                distinct = False
            #       case 2:  new_max in between current_min and current_max
            elif (current_min <= new_max <= current_max) and (new_min <= current_min):
                current_range[0] = new_min
                distinct = False
            #       case 3:  current_range INSIDE new_range
            elif current_min > new_min and current_max < new_max:
                current_range[0] = new_min
                current_range[1] = new_max
                distinct = False
            #       case 4:  new_range INSIDE current_range
            elif new_min > current_min and new_max < current_max:
                distinct = False
                continue

        #       case 5:  new_range OUTSIDE current_range
        if distinct:
            distinct_ranges.append(new_range)
        
        idx = 0
        while idx < len(distinct_ranges):
            current_range = distinct_ranges[idx]
            current_min, current_max = current_range[0], current_range[1]
            jdx = idx+1
            no_merge = True
            while jdx < len(distinct_ranges):
                range_min, range_max = distinct_ranges[jdx][0], distinct_ranges[jdx][1]
                #       case 1:  current_min in between range_min and range_max
                if (range_min <= current_min <= range_max) and (current_max >= range_max):
                    distinct_ranges[jdx][1] = current_max
                    distinct_ranges.pop(idx)
                    no_merge = False
                #       case 2:  current_max in between range_min and range_max
                elif (range_min <= current_max <= range_max) and (current_min <= range_min):
                    distinct_ranges[idx][1] = range_max
                    distinct_ranges.pop(jdx)
                    no_merge = False
                #       case 3:  current_range INSIDE range_min and range_max
                elif range_min > current_min and range_max < current_max:
                    distinct_ranges.pop(idx)
                    no_merge = False
                #       case 4:  new_range INSIDE current_range
                elif current_min > range_min and current_max < range_max:
                    distinct_ranges.pop(jdx)
                    no_merge = False
                else:
                    jdx += 1
            if no_merge:
                idx += 1


        # print(f'AFTER: {distinct_ranges}\n')
    
    # print(distinct_ranges)
    count = 0
    for id_range in distinct_ranges:
        count += id_range[1] - id_range[0] + 1 
    
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
    split_ix = lines.index('')
    ranges = [a.split('-') for a in lines[:split_ix]]
    ranges = [[int(a), int(b)] for a,b in ranges]
    ids = [int(id) for id in lines[split_ix+1:]]
    # print(ranges)
    # print(ids)
    # print(part1(ranges, ids))
    print(part2(ranges))