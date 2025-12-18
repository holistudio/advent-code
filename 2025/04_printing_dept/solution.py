import copy

def part1(grid):
    grid_copy = copy.deepcopy(grid)
    H = len(grid)
    W = len(grid[0])
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "@":
                if (0 < i < H-1) and (0 < j < W-1):
                    window = [grid[i-1][j-1:j+2], grid[i][j-1:j+2], grid[i+1][j-1:j+2]]
                else:
                    if i == 0 and (0 < j < W-1):
                        window = [grid[i][j-1:j+2], grid[i+1][j-1:j+2]]
                    if i == H-1 and (0 < j < W-1):
                        window = [grid[i-1][j-1:j+2], grid[i][j-1:j+2]]
                    if j == 0 and (0 < i < H-1):
                        window = [grid[i-1][:j+2], grid[i][:j+2], grid[i+1][:j+2]]
                    if j == W-1 and (0 < i < H-1):
                        window = [grid[i-1][j-1:], grid[i][j-1:], grid[i+1][j-1:]]
                    if i == 0 and j == 0:
                        window = [grid[i][:j+2], grid[i+1][:j+2]]
                    if i == 0 and j == W-1:
                        window = [grid[i][j-1:], grid[i+1][j-1:]]
                    if i == H-1 and j == 0:
                        window = [grid[i-1][:j+2], grid[i][:j+2]]
                    if i == H-1 and j == W-1:
                        window = [grid[i-1][j-1:], grid[i][j-1:]]
                window = ''.join(window)
                if window.count('@') - 1 < 4:
                    grid_copy[i] = grid_copy[i][:j] + '.' + grid_copy[i][j+1:] 
                    count += 1
    return count, grid_copy

def part2(grid):
    count, grid = part1(grid)
    total = count
    while count > 0:
        count, grid = part1(grid)
        total += count
    return total

if __name__ == "__main__":
    grid = []
    with open("input.txt") as f:
        grid = f.read().split('\n')
    print(part1(grid)[0])
    print(part2(grid))