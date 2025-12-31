def part_1(numbers, operations):
    total = 0
    for nums, op in zip(numbers, operations):
        num1, num2, num3 = nums

        if op == '*':
            total += num1 * num2 * num3
        elif op == '+':
            total += num1 + num2 + num3
        else:
            raise ValueError('Invalid operation string found') 
        
    return total

if __name__ == '__main__':
    with open('example.txt', 'r') as f:
        lines = f.read().split('\n')

        num1 = lines[0].split(' ')
        num2 = lines[1].split(' ')
        num3 = lines[2].split(' ')
        operations = lines[3].split('   ')
    
    num1 = [int(n) for n in num1 if n != '']
    num2 = [int(n) for n in num2 if n != '']
    num3 = [int(n) for n in num3 if n != '']
    numbers = [(n1,n2,n3) for n1, n2, n3 in zip(num1, num2, num3)]

    operations[-1] = operations[-1].rstrip()
    
    print(part_1(numbers, operations))