
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

def part_2(numbers, operations):
    total = 0
    for nums, op in zip(numbers, operations):
        N = len(nums)
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

    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
        N = len(lines[:-1])
        operations = []
        numbers = []
        for i, op in enumerate(lines[-1]):
            
            if op != ' ':
                operations.append(op)
                if not lines[-1][i+1:].isspace():
                    j = i+1
                    while lines[-1][j] == ' ':
                        j += 1
                    num_numbers = j - i - 1
                else:
                    num_numbers = len(lines[-1][i:])

                column = []
                for k in range(i, i+num_numbers):
                    digits = ''
                    for l in range(N):
                        digits += lines[l][k]
                    column.append(int(digits.strip()))
                numbers.append(column)
    print(part_2(numbers, operations))

