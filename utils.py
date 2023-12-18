
def is_end_maze(maze, i, j):
    return maze[i][j] == 'X'

def is_valid(maze, row, col, direction):
    rows = len(maze)
    cols = len(maze[0]) 

    if direction == 'D' and row + 1 < rows and (maze[row + 1][col] == ' ' or maze[row + 1][col] == 'X'):
        return True, row + 1, col
    elif direction == 'U' and row - 1 >= 0 and (maze[row - 1][col] == ' ' or maze[row - 1][col] == 'X'):
        return True, row - 1, col
    elif direction == 'L' and col - 1 >= 0 and (maze[row][col - 1] == ' ' or maze[row][col - 1] == 'X'):
        return True, row, col - 1
    elif direction == 'R' and col + 1 < cols and (maze[row][col + 1] == ' ' or maze[row][col + 1] == 'X'):
        return True, row, col + 1
    else:
        return False, row, col
    
def get_startpoint(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'O':
                return i, j
    return None

def get_goalpoint(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'X':
                return i, j
    return None

def heuristic(row, col, goal_row, goal_col):
    # Manhanttan distance heuristic
    return abs(row - goal_row) + abs(col - goal_col)