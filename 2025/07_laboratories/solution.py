class Beam(object):
    def __init__(self, start_r, start_c):
        self.r = start_r
        self.c = start_c
        self.done = False
        pass

    def step(self):
        self.r += 1
        pass

def display_world(grid_world):
    for line in grid_world:
        print(line)
    print()
    pass

if __name__ == '__main__':
    # load the grid world
    with open('example.txt','r') as f:
        grid_world = f.read().split('\n')
    display_world(grid_world)

    terminal = False
    # find the start position 'S'

    while not terminal:
        # if there's nothing in front of the beam
        # move it a step

        # if the beam has a splitter in front of it
        # move it a step forward and to the left
        # copy it at a new position, two units to the right

        # if the beam is at the end of the grid world, mark it done

        # check if any beams are overlapping existing beams
        # and remove them

        # draw beams on grid world

        # check if all beams are done then terminate the loop

    pass