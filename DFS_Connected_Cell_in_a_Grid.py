def getBiggestRegion_DFS(grid):
    # DFS using stack, no recursion
    max_count = 0
    for i in range(len(grid)):
        # row
        for j in range(len(grid[0])):
            # col
            if grid[i][j] == 1:
                # ignore X or 0
                stack = []
                counter = 0
                stack.append((i, j))
                grid[i][j] = 'X'
                while (stack):
                    visit_stack_top(grid, stack)
                    counter += 1
                max_count = max(max_count, counter)
                #print(i, j, max_count)
                #print_grid(grid)
    return max_count

def print_grid(grid):
    print('BEGIN')
    for row in grid:
        print(row)
    print('END')
    
def visit_stack_top(grid, stack):
    i, j = stack.pop()
    #print('OUT', i, j)
    for di in [-1, 0 , 1]:
        for dj in [-1, 0, 1]:
            # (di or dj) exclude the center pixel
            if (di or dj) and i+di in range(len(grid)) and j+dj in range(len(grid[0])):
                if grid[i+di][j+dj]==1:
                    stack.append((i+di, j+dj))
                    grid[i+di][j+dj] = 'X'
                    #print('IN', i+di, j+dj)

def getBiggestRegion_DFS2(grid):
    # DBF with recursion
    max_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_count = max(max_count, count(grid, i, j))
    return max_count

def count(grid, i, j):
    if i not in range(len(grid)) or j not in range(len(grid[0])):
        return 0
    if grid[i][j] != 1:
        return 0
    counter = 1
    # mark nodes as visited. Otherwise revisits or goes to loop
    # alternatievely we can keep a dictionary to keep record
    #   without modifying the original map
    grid[i][j] = 0
    counter += count(grid, i-1, j-1)
    counter += count(grid, i-1, j)
    counter += count(grid, i-1, j+1)
    counter += count(grid, i, j-1)
    counter += count(grid, i, j+1)
    counter += count(grid, i+1, j-1)
    counter += count(grid, i+1, j)
    counter += count(grid, i+1, j+1)
    return counter

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion_DFS2(grid))
