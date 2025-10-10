def insert_ix(buffer_len, i, x):
    """
    given a circular buffer of a specific length, buffer_len
    and a starting pointer index value, i
    determine the insertion point after moving the pointer
    x steps
    """
    # TODO: compute directly?

    # step forward circular buffer in x steps
    for s in range(x):
        if i < buffer_len-1:
            i += 1
        else:
            i = 0
    # if i == 0:
    #     print(buffer_len, x, buffer_len // x, buffer_len % x)
    return i
    
def main(steps, max_value):
    # starts with a circular buffer containing only the value `0`
    buffer = [0]
    len_buffer = 1

    ix = 0

    after_zero = 0

    # insert_ixs = []

    for v in range(1, max_value+1):
        # print(f'ix_0 = {ix}')

        # step forward circular buffer in _ steps
        ix = insert_ix(len_buffer, ix+1, steps)
        # print(f'ix_1 = {ix}')
        # insert_ixs.append(ix+1)

        # insert value at current position
        # split the buffer into two
        # if len(buffer) > 1:
        #     left_half = buffer[:ix+1]
        #     right_half = buffer[ix+1:]
        # else:
        #     left_half = buffer
        #     right_half = []

        # recombine
        # buffer = left_half + [v] + right_half

        # if buffer[1] != after_zero:
        #     print(buffer[1])
        #     after_zero = buffer[1]
        if ix == 0:
            print(v)
        len_buffer += 1

    # print(f"Final Buffer:  {buffer}")
    # print(f"Last Inserted: {buffer[ix+1]}")
    # print(f"Value After:   {buffer[ix+2]}")
    # print(insert_ixs[:20])

if __name__ == "__main__":
    main(steps=355, max_value=50000000)
    # main(steps=355, max_value=2017)
    # main(steps=3, max_value=2017)