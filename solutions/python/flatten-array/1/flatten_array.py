def flatten(iterable):
    
    result = []
    for row in iterable: 
        if row is None: 
            continue
        elif isinstance(row, list):
            result.extend(flatten(row)) 
        else:
            result.append(row)
    return result