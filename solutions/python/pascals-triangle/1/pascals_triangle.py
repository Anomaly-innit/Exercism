def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    
    previous_rows = rows(row_count - 1)  
    if not previous_rows:
        return [[1]]  
    
    last_row = previous_rows[-1]
    new_row = next_row(last_row)
    return previous_rows + [new_row]
        
def next_row(previous_row):
    new_row = []
    for i in range(len(previous_row) + 1):
        left = previous_row[i-1] if i-1 >= 0 else 0
        right = previous_row[i] if i < len(previous_row) else 0
        new_row.append(left + right)
    return new_row