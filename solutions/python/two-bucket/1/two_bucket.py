from collections import deque 
def measure(bucket_one, bucket_two, goal, start_bucket):
    if goal > max(bucket_one, bucket_two):
        raise ValueError("Goal is greater than both buckets.")

    if start_bucket == "one":
        start_state = (bucket_one, 0)
        forbidden_state = (0, bucket_two)
    else:
        start_state = (0, bucket_two)
        forbidden_state = (bucket_one, 0)
    queue = deque([(start_state, 1)])  
    visited = {start_state}    
    
    
    while queue:
        (b1, b2), actions = queue.popleft()
        
        if b1 == goal:
            return (actions, "one", b2)
        if b2 == goal:
            return (actions, "two", b1)
    
        next_states = [
            (bucket_one, b2),   
            (b1, bucket_two),   
            (0, b2),            
            (b1, 0),            
        ]
    
        new_b1, new_b2 = pour(b1, bucket_one, b2, bucket_two)
        next_states.append((new_b1, new_b2))  
        
        new_b2, new_b1 = pour(b2, bucket_two, b1, bucket_one)
        next_states.append((new_b1, new_b2))  
    
        for state in next_states:
            if state == forbidden_state:
                continue
            if state in visited:
                continue
            visited.add(state)
            queue.append((state, actions + 1))
    raise ValueError("Goal is greater than both buckets.")    
            
def pour(source_amount, source_cap, dest_amount, dest_cap):
    if dest_amount + source_amount <= dest_cap:
        dest_amount += source_amount
        source_amount = 0
    else:
        room = dest_cap - dest_amount
        dest_amount = dest_cap
        source_amount -= room
    return source_amount, dest_amount