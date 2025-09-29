parsed_moves = {}
# parsed_moves = {
#   'x1/3': {
#       "move_type": "x",
#       "parameters": (1,3)
#   }
# }

def read_input(filename: str):
    with open(filename) as f:
        moves = f.read().split(',')
    print(len(moves))
    return moves

def spin(lineup: list, X: int):
    '''Counting from the end, grab X programs from the end and move to front'''
    # split list into two parts, counting from the end
    front = lineup[:-X]
    back = lineup[-X:]

    # swap the front and back into a new list
    lineup = back + front
    return lineup

def exchange(lineup: list, a: int, b: int):
    '''Swapping based on position in the lineup'''
    # get programs at each location
    program_a = lineup[a]
    program_b = lineup[b]
    
    # switch the two
    lineup[a] = program_b
    lineup[b] = program_a
    return lineup

def partner(lineup: list, a: str, b: str):
    '''Swapping based on name in the lineup'''
    # find the index of program
    location_a = lineup.index(a)
    location_b = lineup.index(b)

    # exchange based indices of each program
    lineup = exchange(lineup, location_a, location_b)
    return lineup

def store_move(move: str, move_type: str, parameters: tuple):
    parsed_moves[move] = {
        "move_type": move_type,
        "parameters": parameters
    }
    pass

def parse_move(move: str):
    # NOTE: Revisit
    # - can we reduce the number of if statement checks?
    # - how do we not repeated parse the same command?

    # check parsed_moves has the move string already
    if move in parsed_moves.keys():
        # print("WE'VE BEEN HERE!")
        move_type = parsed_moves[move]["move_type"]
        parameters = parsed_moves[move]["parameters"]
        return move_type, parameters
    else:
        # get move type based on the first letter
        move_type = move[0]

        # create a list of parameters based on move_type
        if move_type == 's':
            X = int(move[1:])
            store_move(move, move_type, (X))
            return move_type, X
        elif move_type == 'x':
            move_components = move[1:]
            A = int(move_components.split('/')[0])
            B = int(move_components.split('/')[1])
            store_move(move, move_type, (A, B))
            return move_type, (A, B)
        elif move_type == 'p':
            move_components = move[1:]
            A = move_components.split('/')[0]
            B = move_components.split('/')[1]
            store_move(move, move_type, (A, B))
            return move_type, (A, B)
        else:
            return ValueError('Dance move not recognized...')

def test_spin(lineup: list, move: str):
    print(f'Original\n{lineup}')
    move_type, parameters = parse_move(move)
    if move_type == 's':
        print(f'Move: {move}\n')
        X = parameters
        new_lineup = spin(lineup, X)
        print(f'Result\n{new_lineup}\n\n')
        return new_lineup

def test_exchange(lineup: list, move: str):
    print(f'Original\n{lineup}')
    move_type, parameters = parse_move(move)
    if move_type == 'x':
        print(f'Move: {move}\n')
        A, B = parameters
        new_lineup = exchange(lineup, A, B)
        print(f'Result\n{new_lineup}\n\n')
        return new_lineup

def test_partner(lineup: list, move: str):
    print(f'Original\n{lineup}')
    move_type, parameters = parse_move(move)
    if move_type == 'p':
        print(f'Move: {move}\n')
        move_components = move[1:]
        A, B = parameters
        new_lineup = partner(lineup, A, B)
        print(f'Result\n{new_lineup}\n\n')
        return new_lineup

def main(programs, moves):

    print(f'Original\n{programs}\n')

    # for each move
    for move in moves:
        # parse the string that describes each move
        # NOTE: re-visit efficient way to do it
        move_type, parameters = parse_move(move)

        # call the corresponding function spin/exchange/partner
        # with the parameters
        if move_type == 's':
            X = parameters
            programs = spin(programs, X)
        elif (move_type == 'x'):
            A, B = parameters
            programs = exchange(programs, A, B)
        elif (move_type == 'p'):
            A, B = parameters
            programs = partner(programs, A, B)

    print(f'Result\n{programs}')
    pass

if __name__ == "__main__":
    # line = test_spin(programs, 's1')
    # line = test_exchange(line, 'x3/4')
    # line = test_partner(line, 'pe/b')

    # programs = ['a','b','c','d','e']
    # moves = ['s1', 'x3/4', 'pe/b']
    # moves = ['s1', 'x3/4', 'pe/b', 'x3/4']

    programs = [chr(x) for x in range(97,97+16)]
    
    # read input.txt
    moves = read_input('input.txt')
    # moves = ['s1', 'x3/4', 'pe/b']

    main(programs, moves)

    # print(parsed_moves)