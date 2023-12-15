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

