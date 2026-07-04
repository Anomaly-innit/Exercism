def tick(matrix):
    result = []
    offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for row_num, row in enumerate(matrix):
        new_row = []
        for col_num, cell in enumerate(row):
            live_neighbors = 0
            for dr, dc in offsets:
                neighbor_row = row_num + dr
                neighbor_col = col_num + dc
                if 0 <= neighbor_row < len(matrix) and 0 <= neighbor_col < len(row):
                    live_neighbors += matrix[neighbor_row][neighbor_col]
            if cell == 1 and live_neighbors in (2, 3):
                new_row.append(1)
            elif cell == 0 and live_neighbors == 3:
                new_row.append(1)
            else:
                new_row.append(0)
        result.append(new_row)
    return result