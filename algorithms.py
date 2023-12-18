import queue
import time

import utils as ut


async def BFS(maze):
    start_time = time.time()
    visited = set()  # Keep track of visited positions
    q = queue.Queue()
    visited_states = []
    start_row, start_col = ut.get_startpoint(maze)
    q.put((start_row, start_col, ''))  # Include current position and trajectory in the queue

    while not q.empty():
        row, col, trajectory = q.get()

        if (row, col) in visited:
            continue  # Skip if the position has been visited before

        visited.add((row, col))

        for direction in ['D', 'U', 'L', 'R']:
            valid, new_row, new_col = ut.is_valid(maze, row, col, direction)

            if valid:
                new_trajectory = f'{trajectory}{direction}'
                q.put((new_row, new_col, new_trajectory))
                visited_states.append(new_trajectory)
            if ut.is_end_maze(maze, new_row, new_col):
                return { 
                    'trajectory': new_trajectory,
                    'time': time.time() - start_time,
                    'states': visited_states
                    }
    return 'No solution found'

async def DFS(maze):
    start_time = time.time()
    visited = set()  # Keep track of visited positions
    visited_states = []
    stack = []
    start_row, start_col = ut.get_startpoint(maze)
    stack.append((start_row, start_col, ''))  # Include current position and trajectory in the stack

    while stack:
        row, col, trajectory = stack.pop()

        if (row, col) in visited:
            continue  # Skip if the position has been visited before

        visited.add((row, col))

        for direction in ['D', 'U', 'L', 'R']:
            valid, new_row, new_col = ut.is_valid(maze, row, col, direction)

            if valid:
                new_trajectory = f'{trajectory}{direction}'
                stack.append((new_row, new_col, new_trajectory))
                visited_states.append(new_trajectory)

            if ut.is_end_maze(maze, new_row, new_col):
                return { 
                    'trajectory': new_trajectory,
                    'time': time.time() - start_time,
                    'states': visited_states
                    }

    return 'No solution found'

async def greedy_search(maze):
    start_time = time.time()
    start_row, start_col = ut.get_startpoint(maze)
    goal_row, goal_col = ut.get_goalpoint(maze)
    visited_states = []

    priority_queue = queue.PriorityQueue()
    priority_queue.put((ut.heuristic(start_row, start_col, goal_row, goal_col), start_row, start_col, ''))

    visited = set()

    while not priority_queue.empty():
        _, row, col, trajectory = priority_queue.get()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        if ut.is_end_maze(maze, row, col):
            return { 
                'trajectory': new_trajectory,
                'time': time.time() - start_time,
                'states': visited_states
            }

        for direction in ['D', 'U', 'L', 'R']:
            valid, new_row, new_col = ut.is_valid(maze, row, col, direction)

            if valid:
                new_trajectory = f'{trajectory}{direction}'
                priority_queue.put((ut.heuristic(new_row, new_col, goal_row, goal_col), new_row, new_col, new_trajectory))
                visited_states.append(new_trajectory)

    return 'No solution found'

async def A_star(maze):
    start_time = time.time()
    start_row, start_col = ut.get_startpoint(maze)
    goal_row, goal_col = ut.get_goalpoint(maze)
    visited_states = []
    priority_queue = queue.PriorityQueue()
    priority_queue.put((ut.heuristic(start_row, start_col, goal_row, goal_col), 0, start_row, start_col, ''))

    visited = set()

    while not priority_queue.empty():
        _, cost, row, col, trajectory = priority_queue.get()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        if ut.is_end_maze(maze, row, col):
            return { 
                'trajectory': new_trajectory,
                'time': time.time() - start_time,
                'states': visited_states
            }

        for direction in ['D', 'U', 'L', 'R']:
            valid, new_row, new_col = ut.is_valid(maze, row, col, direction)

            if valid:
                new_trajectory = f'{trajectory}{direction}'
                new_cost = cost + 1 + ut.heuristic(new_row, new_col, goal_row, goal_col)
                priority_queue.put((new_cost, cost + 1, new_row, new_col, new_trajectory))
                visited_states.append(new_trajectory)

    return 'No solution found'