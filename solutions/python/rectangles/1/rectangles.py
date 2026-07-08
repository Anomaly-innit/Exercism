def rectangles(strings):
    count = 0
    for row1 in range(len(strings)):
        for row2 in range(row1 + 1, len(strings)):
            for col1 in range(len(strings[0])):
                for col2 in range(col1 + 1, len(strings[0])):
                    if (strings[row1][col1] == "+" and strings[row1][col2] == "+" and 
                        strings[row2][col1] == "+" and strings[row2][col2] == "+" and
                        is_horizontal_edge(strings[row1], col1, col2) and
                        is_horizontal_edge(strings[row2], col1, col2) and
                        is_vertical_edge(strings, col1, row1, row2) and
                        is_vertical_edge(strings, col2, row1, row2)):
                        count += 1
    return count
                        
def is_horizontal_edge(row, col1, col2):
    for col in range(col1, col2 + 1):
        if row[col] not in "-+":
            return False
    return True
    
def is_vertical_edge(strings, col, row1, row2):
    for row in range(row1, row2 + 1):
        if strings[row][col] not in "|+":
            return False
    return True

