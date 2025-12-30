def part1(ranges, ids):
    fresh = 0
    for id in ids:
        for id_range in ranges:
            if id_range[0] <= id <= id_range[1]:
                fresh += 1
                break
    return fresh

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