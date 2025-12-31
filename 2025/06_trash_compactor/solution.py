
def part_1(numbers, operations):
    total = 0
    N = len(numbers[0])
    for nums, op in zip(numbers, operations):
        num1 = nums[0]
        if op == '*':
            for i in range(1,N):
                num1 = num1 * nums[i]
        elif op == '+':
            for i in range(1,N):
                num1 = num1 + nums[i]
        else:
            print(op)
            raise ValueError('Invalid operation string found') 
        total += num1
    return total

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')

        nums = []
        N = len(lines[:-1])
        for line in lines[:-1]:
            num = line.split(' ')
            num = [int(n) for n in num if n != '']
            nums.append(num)
        
        numbers = []
        for i in range(len(nums[0])):
            column = []
            for j in range(N):
                column.append(nums[j][i])
            numbers.append(column)

        operations = lines[-1]
        operations = [o for o in operations if o !=' ']

    print(part_1(numbers, operations))