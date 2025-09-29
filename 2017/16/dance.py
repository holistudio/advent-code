programs = ['a','b','c','d','e']

moves = ['s1', 'x3/4', 'pe/b']

def spin(lineup: list, amount_of_moves: int):
    '''Counting from the end, grab x letters from the end based on amount of moves and move to front'''
    return lineup

def exchange(lineup: list, a: int, b:int):
    '''Swapping based on position in the lineup'''
    # get programs at each location
    program_a = lineup[a]
    program_b = lineup[b]
    
    # switch the two
    lineup[a] = program_b
    lineup[b] = program_a
    return lineup

def partner(lineup: list, a: str, b:str):
    '''Swapping based on name in the lineup'''
    # find the index of program
    location_a = lineup.index(a)
    location_b = lineup.index(b)

    # exchange based indices of each program
    lineup = exchange(lineup, location_a, location_b)
    return lineup

def main():
    # given list of moves

    # parse the string that describes each move
    # NOTE: re-visit efficient way to do it


    # call the corresponding function spin/exchange/partner
    # with the parameters

    # programs = spin(programs, a)
    pass