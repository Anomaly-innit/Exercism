def spiral_matrix(size):
   
    matrix = [[0] * size for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #              right    down     left      up

    row, col, direction_index = 0, 0, 0
    
    for num in range(1, size * size + 1):
        matrix[row][col] = num       # matrix[0][0] = 1
        dr, dc = directions[direction_index]  # directions[0] = (0, 1)
        next_row, next_col = row + dr, col + dc  # next_row, next_col = 0 + 0, 0 + 1
    
        
        if not (0 <= next_row < size and 0 <= next_col < size) or matrix[next_row][next_col] != 0:
            direction_index = (direction_index + 1) % 4  # turn clockwise
            dr, dc = directions[direction_index]
        
        row, col = row + dr, col + dc

    return matrix
    