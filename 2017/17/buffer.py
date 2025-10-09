def insert_ix(buffer_len, i, x):
    """
    given a buffer of a specific
    """
    # TODO: compute directly?

    # step forward circular buffer in x steps
    for s in range(x):
        if i < buffer_len-1:
            i += 1
        else:
            i = 0
        # print(i)
    return i
    
def main(x):
    # starts with a circular buffer containing only the value `0`
    buffer = [0]

    ix = 0

    # for v in range(1, 2017+1):
    for v in range(1, 9+1):
        # print(f'ix_0 = {ix}')

        # step forward circular buffer in x steps
        ix = insert_ix(len(buffer), ix+1, x)
        # print(f'ix_1 = {ix}')

        # insert value at current position
        # split the buffer into two
        if len(buffer) > 1:
            left_half = buffer[:ix+1]
            right_half = buffer[ix+1:]
        else:
            left_half = buffer
            right_half = []

        # recombine
        buffer = left_half + [v] + right_half

    print(f"Final Buffer:  {buffer}")
    print(f"Last Inserted: {buffer[ix+1]}")
    print(f"Value After:   {buffer[ix+2]}")

if __name__ == "__main__":
    main(3)