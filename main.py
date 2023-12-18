import queue

import utils as ut

def heuristic(row, col, goal_row, goal_col):
    # Manhanttan distance heuristic
    return abs(row - goal_row) + abs(col - goal_col)

def A_star(maze):
    rows = len(maze)
    cols = len(maze[0])

    start_row, start_col = ut.get_startpoint(maze)
    goal_row, goal_col = ut.get_goalpoint(maze)

    priority_queue = queue.PriorityQueue()
    priority_queue.put((heuristic(start_row, start_col, goal_row, goal_col), 0, start_row, start_col, ''))

    visited = set()

    while not priority_queue.empty():
        _, cost, row, col, trajectory = priority_queue.get()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        if ut.is_end_maze(maze, row, col):
            return trajectory

        for direction in ['D', 'U', 'L', 'R']:
            valid, new_row, new_col = ut.is_valid(maze, row, col, direction)

            if valid:
                new_trajectory = f'{trajectory}{direction}'
                new_cost = cost + 1 + heuristic(new_row, new_col, goal_row, goal_col)
                priority_queue.put((new_cost, cost + 1, new_row, new_col, new_trajectory))

    return 'No solution found'

def greedy_search(maze):
    rows = len(maze)
    cols = len(maze[0])

    start_row, start_col = ut.get_startpoint(maze)
    goal_row, goal_col = ut.get_goalpoint(maze)

    priority_queue = queue.PriorityQueue()
    priority_queue.put((heuristic(start_row, start_col, goal_row, goal_col), start_row, start_col, ''))

    visited = set()

    while not priority_queue.empty():
        _, row, col, trajectory = priority_queue.get()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        if ut.is_end_maze(maze, row, col):
            return trajectory

        for direction in ['D', 'U', 'L', 'R']:
            valid, new_row, new_col = ut.is_valid(maze, row, col, direction)

            if valid:
                new_trajectory = f'{trajectory}{direction}'
                priority_queue.put((heuristic(new_row, new_col, goal_row, goal_col), new_row, new_col, new_trajectory))

    return 'No solution found'


if __name__ == '__main__':
    maze = [
        [' ', '#', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', '#', ' ', ' '],
        ['X', '#', 'O', ' '],
    ]
    for x in maze:
        print(x)
    print(greedy_search(maze))