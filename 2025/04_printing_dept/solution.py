import copy

def part1(grid):
    grid_copy = copy.deepcopy(grid)
    H = len(grid)
    W = len(grid[0])
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "@":
                row_start = max(0, i-1)
                row_end = min(H-1, i+1)
                col_start = max(0, j-1)
                col_end = min(W-1, j+1)

                window = []
                for r in range(row_start, row_end+1):
                    window_row = ""
                    for c in range(col_start, col_end+1):
                        window_row += grid[r][c]
                    window.append(window_row)

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