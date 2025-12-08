from collections import OrderedDict

def part1(batteries):
    total_joltage = 0
    for bank in batteries:
        ints = [int(c) for c in bank]
        ix = len(ints)
        if len(ints[ints.index(max(ints[:ix])):])==1:
            ix -= 1
        max_digit = str(max(ints[:ix]))
        next_max_digit = str(max(ints[ints.index(max(ints[:ix]))+1:]))
        max_joltage = int(max_digit + next_max_digit)
        total_joltage += max_joltage
    return total_joltage

if __name__ == '__main__':
    with open('input.txt') as f:
        batteries = f.read().split('\n')
    print(part1(batteries))