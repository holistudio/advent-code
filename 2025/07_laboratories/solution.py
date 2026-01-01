class Beam(object):
    def __init__(self, start_r, start_c):
        self.r = start_r
        self.c = start_c
        pass

    def step(self):
        self.r += 1
        pass

if __name__ == '__main__':
    # load the grid world

    # find the start position 'S'

    # if there's nothing in front of the beam
    # move it a step

    # if the beam has a splitter in front of it
    # move it a step forward and to the left
    # copy it at a new position, two units to the right

    # check if any beams are overlapping existing beams
    # and remove them

    # draw beams on grid world
    pass