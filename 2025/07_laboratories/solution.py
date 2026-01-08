import copy
import datetime

# class Beam(object):
#     def __init__(self, start_r, start_c):
#         self.r = start_r
#         self.c = start_c
#         self.done = False
#         pass

#     def step(self):
#         self.r += 1
#         pass


def display_world(grid_world):
    for line in grid_world:
        print(line)
    print()
    pass

if __name__ == '__main__':
    initial_beam = {
        "r":0,
        "c":0,
        "done": False
    }

    # load the grid world
    with open('input.txt','r') as f:
        grid_world = f.read().split('\n')
    # display_world(grid_world)

    R = len(grid_world)
    C = len(grid_world[0])

    # find the start position 'S'
    start_c = grid_world[0].index('S')

    # initial_beam = Beam(0, start_c)
    initial_beam['c'] = start_c

    beams = [initial_beam]

    split_count = 0
    terminal = False

    while not terminal:
        start_time = datetime.datetime.now()
        prev_len = len(beams)

        for beam in beams:
            if not beam['done']:
                if beam['r'] < R-1:
                    # if there's nothing in front of the beam
                    # move it a step
                    beam['r'] += 1
                    # if the beam has a splitter in front of it
                    if grid_world[beam['r']][beam['c']] == '^':
                        split_count += 1
                        # copy it at a new position, 1 unit to the right and 1 unit backward
                        beams.append(copy.deepcopy(beam))
                        beams[-1]['c'] += 1
                        beams[-1]['r'] -= 1

                        # move it to the left
                        beam['c'] -= 1
                else:
                    # if the beam is at the end of the grid world, mark it done
                    beam['done'] = True

        # split beams
        for beam in beams:
            if not beam['done']:
                # if the beam has a splitter in front of it
                if grid_world[beam['r']][beam['c']] == '^':
                    split_count += 1
                    # copy it at a new position, 1 unit to the right
                    beams.append(copy.deepcopy(beam))
                    beams[-1]['c'] += 1

                    # move it a step forward and to the left
                    beam['c'] -= 1

        # check if any beams are overlapping existing beams
        # and remove them
        for beam in beams:
            if grid_world[beam['r']][beam['c']] == '|':
                beams.pop(beams.index(beam))

        i = 0
        while i < (len(beams) - 1):
            j = i+1
            while j < len(beams):
                beam_i = beams[i]
                beam_j = beams[j]
                if beam_i['r'] == beam_j['r'] and beam_i['c'] == beam_j['c']:
                    beams.pop(j)
                else:
                    j += 1
            i += 1

        # draw beams on grid world
        num_done = 0
        for beam in beams:
            grid_world[beam['r']] = grid_world[beam['r']][:beam['c']] + '|' + grid_world[beam['r']][beam['c']+1:]
            if beam['done']:
                num_done += 1

        # check if all beams are done then terminate the loop
        # if num_done == len(beams):
        #     terminal = True
        terminal = True
        for beam in beams:
            if not beam['done']:
                terminal = False
                break
    
    display_world(grid_world)

    print(split_count)
    # print(len(beams))
    pass