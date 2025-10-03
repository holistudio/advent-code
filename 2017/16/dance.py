import datetime
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
    # print(len(moves))
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

def make_move(lineup: list, move: str):
    # parse the string that describes each move
    move_type, parameters = parse_move(move)

    # call the corresponding function spin/exchange/partner
    # with the parameters
    if move_type == 's':
        X = parameters
        lineup = spin(lineup, X)
    elif (move_type == 'x'):
        A, B = parameters
        lineup = exchange(lineup, A, B)
    elif (move_type == 'p'):
        A, B = parameters
        lineup = partner(lineup, A, B)
    return lineup
    
def dance (lineup: list, moves: list):
    # for each move
    for move in moves:
        lineup = make_move(lineup, move)
    return lineup

def main():
    # given list of programs a-p
    programs = [chr(x) for x in range(97,97+16)]

    # read input.txt
    moves = read_input('input.txt')

    print(f'Original\n{"".join(programs)}\n')

    programs = dance(programs, moves)

    print(f'Part 1 Result\n{"".join(programs)}\n')

    # Keeping the positions they ended up in from their previous dance
    # including the first dance, a total of one billion (1000000000) times.
    start_time = datetime.datetime.now()
    for i in range(1000000000-1):
        programs = dance(programs, moves)
        if i % 1000 == 0:

            print(i, datetime.datetime.now()-start_time)

    print(f'Part 2 Result\n{"".join(programs)}\n')

    
    pass

if __name__ == "__main__":
    main()