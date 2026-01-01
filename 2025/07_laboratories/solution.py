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

    R = len(grid_world)
    C = len(grid_world[0])

    # find the start position 'S'
    start_c = grid_world[0].index('S')
    initial_beam = Beam(0, start_c)

    beams = [initial_beam]

    terminal = False
    while not terminal:
        for beam in beams:
            if beam.r < R-1:
                # if there's nothing in front of the beam
                # move it a step
                beam.step()
                
                # if the beam has a splitter in front of it
                # move it a step forward and to the left
                # copy it at a new position, two units to the right

            # if the beam is at the end of the grid world, mark it done
            else:
                beam.done = True

        # check if any beams are overlapping existing beams
        # and remove them

        # draw beams on grid world
        num_done = 0
        for beam in beams:
            grid_world[beam.r] = grid_world[beam.r][:beam.c] + '|' + grid_world[beam.r][beam.c+1:]
            if beam.done:
                num_done += 1

        # check if all beams are done then terminate the loop
        if num_done == len(beams):
            terminal = True
    
    display_world(grid_world)
    pass