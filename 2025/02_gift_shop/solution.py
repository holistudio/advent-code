def part1(input_list):
    sum = 0
    for range_item in input_list:
        range_strs = range_item.split('-')
        start_id, end_id = int(range_strs[0]), int(range_strs[1])
        for id in range(start_id, end_id+1):
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

def part2(input_list):
    sum = 0
    for range_item in input_list:
        range_strs = range_item.split('-')
        start_id, end_id = int(range_strs[0]), int(range_strs[1])
        for id in range(start_id, end_id+1):
            id_str = str(id)
            seq_len = len(id_str)

            tried_seqs = []
            sliding_window_len = 1
            found = False
            while not found and (sliding_window_len <= (seq_len // 2)):
                repeats = seq_len // sliding_window_len
                for i in range(0,seq_len-sliding_window_len):
                    sub_id = id_str[i:i+sliding_window_len]
                    if sub_id not in tried_seqs:
                        tried_seqs.append(sub_id)
                        candidate_seq = ''
                        for j in range(repeats):
                            candidate_seq += sub_id
                        if candidate_seq == id_str:
                            sum += id
                            found = True
                            break
                sliding_window_len +=1
    return sum

if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = f.read().split(',')
    print(f"Part 1 Answer: {part1(input_list)}")
    print(f"Part 2 Answer: {part2(input_list)}")