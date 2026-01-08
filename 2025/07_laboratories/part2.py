


# load the grid world
with open('example.txt','r') as f:
    grid_world = f.read().split('\n')
# display_world(grid_world)

R = len(grid_world)
C = len(grid_world[0])

def single_beam(start_row, start_col):
    row = start_row
    col = start_col
    if row < R-1:
        row += 1
        if grid_world[row][col] == '^':
            return single_beam(row, col+1) + single_beam(row,col-1)
        else:
            return single_beam(row, col)
    else:
        return 1

# find the start position 'S'
start_c = grid_world[0].index('S')

print(single_beam(0,start_c))