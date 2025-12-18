def part1(grid):
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
                    # print(i,j, window)
                    count += 1
    return count



if __name__ == "__main__":
    grid = []
    with open("input.txt") as f:
        grid = f.read().split('\n')
    print(part1(grid))