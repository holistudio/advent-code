from collections import OrderedDict

def part1(batteries):
    total_joltage = 0
    for bank in batteries:
        bank_ints = [int(c) for c in bank]
        digits = list(OrderedDict.fromkeys(bank_ints))
        # print(digits)
        ix = len(digits)
        while len(digits[digits.index(max(digits[:ix])):])==1:
            ix -= 1
        # if there are more digits after it, get the largest digit of those
        max_digit = str(max(digits[:ix]))
        next_max_digit = str(max(digits[digits.index(max(digits[:ix]))+1:]))
        max_joltage = int(max_digit + next_max_digit)
        # print(max_joltage)
        total_joltage += max_joltage
    return total_joltage

if __name__ == '__main__':
    with open('example.txt') as f:
        batteries = f.read().split('\n')
    print(part1(batteries))