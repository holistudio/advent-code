def part1(input_list):
    sum = 0
    for range_item in input_list:
        range_strs = range_item.split('-')
        start_id, end_id = int(range_strs[0]), int(range_strs[1])
        # print(start_id,end_id)
        for id in range(start_id, end_id+1):
            # print(id)
            id_str = str(id)

            # get id sequence length
            seq_len = len(id_str)
            
            # if length is odd, ignore
            # if length is even, chop the id in half
            if seq_len % 2 == 0:
                sub_len = seq_len // 2
                half1 = int(id_str[:sub_len])
                half2 = int(id_str[sub_len:])
                # compare the two halves -> invalid?
                if half1 == half2:
                    sum += id
            
    return sum

if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = f.read().split(',')
    print(part1(input_list))