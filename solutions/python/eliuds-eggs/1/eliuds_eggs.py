def egg_count(display_value):
    
    result = 0
    if display_value == 0:
        return 0
    while display_value > 0:
        
        if display_value & 1 == 1:
            result+=1
        display_value = display_value >> 1

    return result
