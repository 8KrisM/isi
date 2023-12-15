import queue

if __name__ == '__main__':
    maze = [
        [' ', '#', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', '#', ' ', ' '],
        ['X', '#', 'O', ' '],
    ]
    for x in maze:
        print(x)
    print(DFS())