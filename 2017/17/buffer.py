def insert_ix(buffer_len, i, x):
    """
    given a buffer of a specific
    """
    # TODO: compute directly?

    # step forward circular buffer in x steps
    for s in range(x):
        if s < buffer_len:
            i += 1
        else:
            i = 0
    return i
    
def main(x):
    # starts with a circular buffer containing only the value `0`
    buffer = [0]

    ix = 0

    # for v in range(1, 2017+1):
    for v in range(1, 8+1):
        # step forward circular buffer in x steps
        ix = insert_ix(len(buffer), ix, x)

        if len(buffer) > 1:
            # insert value=1 at current position
            # split the buffer into two
            left_half = buffer[:ix]
            right_half = buffer[ix:]
        else:
            left_half = buffer
            right_half = []

        # recombine
        buffer = left_half + [v] + right_half

        print(buffer)

        # repeat but now insert value=2

if __name__ == "__main__":
    main(3)