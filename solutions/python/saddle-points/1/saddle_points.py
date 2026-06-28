def saddle_points(matrix):

    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("irregular matrix")
            
    result = []
    
    for row_num, row in enumerate(matrix, start=1): #  [9, 8, 7, 8],
        
        for col_num, num in enumerate(row, start=1):
            
            if num == max(row):
                column = [r[col_num-1] for r in matrix]
                
                if num == min(column):
                    result.append({"row": row_num, "column": col_num})
                    
    return result
            