def pour_water(n, grid):
    # Function to check if a cell (x, y) is within the grid boundaries
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    # Function to check if water can flow from cell (x, y) based on its level compared to the current water level
    def can_flow(x, y, level):
        return is_valid(x, y) and grid[x][y] <= level

    # Function to spread water to neighboring cells if it can flow, updating grid and print_grid
    def spread_water(x, y, level):
        if can_flow(x, y, level):
            grid[x][y] = level  # Update the grid with the current water level
            print_grid[x][y] = "W"  # Update the print_grid to mark the cell as 'W'
            left = False
            right = False

            for cell in print_grid:
                if cell[0] == "W":
                    left = True
                    break
                if cell[n - 1] == "W":
                    right = True
                    break

            if ("W" in print_grid[n - 1]) or ("W" in print_grid[0]) or left or right:
                return 1
            queue.append((x, y))  # Add the cell to the queue for further processing
            return 0

    # Initialize water level with the value at the center of the grid
    water_level = grid[center][center]
    print_grid[center][center] = "W"  # Mark the center cell as 'W' in the print_grid
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]  # Define directions: right, down, left, up

    queue = [(center, center)]  # Start with the center cell
    visited = set(queue)  # Keep track of visited cells

    # Simulate water flow
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                status = spread_water(new_x, new_y, water_level)
                if status:
                    return


# Getting input values
n = int(input())  # Get grid dimensional number
center = n // 2  # Calculate the center index of the grid
grid = []  # Initializing an empty grid
print_grid = []  # Initializing an empty wet or dry status grid

# Get row wise grid input 'n' times
for i in range(0, n):
    row = list(map(int, input().split()))  # Get row of elevation values
    grid.append(row)  # Create the grid based on the input values
    print_grid.append(
        n * ["."]
    )  # Initialize print_grid with all cells as '.' indicating as dry cells at first

pour_water(n, grid)  # Start the water pouring simulation

while True:
    left_side = False
    right_side = False

    for cell in print_grid:
        if cell[0] == "W":
            left_side = True
            break
        if cell[n - 1] == "W":
            right_side = True
            break

    if ("W" in print_grid[n - 1]) or ("W" in print_grid[0]) or left_side or right_side:
        # If water reached the edges or sides, print the final grid
        for row in print_grid:
            print("".join(row))
        break
    else:
        grid[center][center] += 1  # Increment the water level at the center
        pour_water(
            n, grid
        )  # Continue the water flow simulation with the increased water level
