# Maze Escape Game

import random

# Function to generate a maze with walls and empty spaces
def generate_maze(size):
    maze = [["#" for _ in range(size)] for _ in range(size)]  # Initialize maze with walls
    for row in range(1, size - 1):
        for col in range(1, size - 1):
            if random.random() < 0.7:  # Adjust the density of walls (70% of cells are walls)
                maze[row][col] = " "  # Assign empty space to some cells
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print("".join(row))

# Function to find neighboring cells for generating paths
def find_neighbors(cell, size):
    neighbors = []
    row, col = cell

    # Add neighboring cells (up, down, left, right) if they are within bounds
    if row > 1: neighbors.append((row - 2, col))
    if row < size - 2: neighbors.append((row + 2, col))
    if col > 1: neighbors.append((row, col - 2))
    if col < size - 2: neighbors.append((row, col + 2))

    random.shuffle(neighbors)  # Shuffle neighbors to randomize path generation
    return neighbors

# Recursive function to generate a path through the maze
def generate_path(maze, cell, visited):
    maze[cell[0]][cell[1]] = " "  # Mark current cell as a path

    visited.add(cell)
    neighbors = find_neighbors(cell, len(maze))

    for neighbor in neighbors:
        if neighbor not in visited:
            row, col = neighbor
            # Carve a path by removing walls between the current cell and the neighbor
            if row == cell[0]:
                maze[row][min(col, cell[1]) + 1] = " "
            else:
                maze[min(row, cell[0]) + 1][col] = " "
            generate_path(maze, neighbor, visited)

# Main game function
def maze_game(size):
    maze = generate_maze(size)  # Generate the maze
    start = (random.randint(0, size // 2) * 2, 0)  # Random starting point on the left edge
    end = (random.randint(0, size // 2) * 2, size - 1)  # Random ending point on the right edge
    
    generate_path(maze, start, set())  # Generate path through the maze

    player = start
    maze[start[0]][start[1]] = "S"  # Mark start point
    maze[end[0]][end[1]] = "E"  # Mark end point
    print_maze(maze)  # Display maze to player

    print("S: Start, E: Exit")

    while player != end:
        move = input("Enter direction (up: u/ down: d/ left: l/ right: r): ").lower()

        next_row, next_col = player
        if move == "u":
            next_row -= 1
        elif move == "d":
            next_row += 1
        elif move == "l":
            next_col -= 1
        elif move == "r":
            next_col += 1
        else:
            print("Invalid move. Use up/down/left/right.")
            continue

        # Check if the next move is valid (within bounds and not a wall)
        if 0 <= next_row < size and 0 <= next_col < size and maze[next_row][next_col] != "#":
            if maze[next_row][next_col] != "#" and maze[(player[0] + next_row) // 2][(player[1] + next_col) // 2] != "#":
                maze[player[0]][player[1]] = " "  # Clear previous position
                player = (next_row, next_col)  # Update player's position
                maze[player[0]][player[1]] = "P"  # Mark new position as player

        print_maze(maze)  # Display maze with updated player position

    print("Congratulations! You reached the exit.")

# Get maze size from user input
maze_size = int(input("Enter maze size (odd number): "))
if maze_size % 2 == 0:
    maze_size += 1  # Make sure maze size is odd
maze_game(maze_size)  # Start the maze game
