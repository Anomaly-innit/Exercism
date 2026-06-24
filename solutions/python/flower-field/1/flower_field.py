def annotate(garden):
    if not garden:
        return []
    first_length = len(garden[0])
    for row in garden:
        if len(row) != first_length:
            raise ValueError("The board is invalid with current input.")
    for row in garden:
        for char in row:
            if char not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")
    # Function body starts here
    r = 0
    c = 0

    result = [["*" if char == "*" else 0 for char in row] for row in garden]  #result = [ "0", "*", "*" ...]

    for r, row in enumerate(garden):
        for c, char in enumerate(row):
            if char == "*":
                for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(garden) and 0 <= nc < len(row):
                        if result[nr][nc] != "*":
                            result[nr][nc] += 1
    output = []
    for row in result:
        row_string = ""
        for cell in row:
            if cell == 0:
                row_string += " "
            else:
                row_string += str(cell)
        output.append(row_string)
    return output   
