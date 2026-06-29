def sum_of_multiples(limit, multiples):
    result = []
    for item in multiples:
         
        if item == 0 or item >= limit:
            
            continue
        item_copy = item
            
        while item_copy < limit:
            result.append(item_copy)
            item_copy += item    
                
    return sum(set(result))
