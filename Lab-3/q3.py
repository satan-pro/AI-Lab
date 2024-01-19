def is_valid_move(maze, x, y, visited):
    rows, columns = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < columns and maze[x][y] == 0 and not visited[x][y]

def solve_maze_dfs(maze):
    rows, columns = len(maze), len(maze[0])
    visited = [[False for _ in range(columns)] for _ in range(rows)]

    def dfs(x, y):
        if x == rows - 1 and y == columns - 1:  # Reached the exit
            return True

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            if is_valid_move(maze, new_x, new_y, visited):
                visited[new_x][new_y] = True
                if dfs(new_x, new_y):
                    return True  # Exit found in this path
                visited[new_x][new_y] = False  # Backtrack

        return False  # No valid move

    visited[0][0] = True  # Mark the entrance as visited
    if dfs(0, 0):
        print("Maze solved!")
    else:
        print("No solution found.")

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

solve_maze_dfs(maze)
