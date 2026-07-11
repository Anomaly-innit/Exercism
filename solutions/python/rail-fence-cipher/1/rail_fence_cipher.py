def encode(message, rails):
    
    rails_lists = [[] for _ in range(rails)]
    current_rail = 0
    direction = 1
    
    for char in message:
        rails_lists[current_rail].append(char)
        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
        current_rail += direction
        
    result = "".join("".join(rail) for rail in rails_lists)
    return result

def decode(encoded_message, rails):
    pattern = get_rail_pattern(len(encoded_message), rails)
    
    rail_chunks = []
    start = 0
    for rail_num in range(rails):
        count = pattern.count(rail_num)
        rail_chunks.append(list(encoded_message[start:start+count]))
        start += count
    
    result = []
    for rail_num in pattern:
        result.append(rail_chunks[rail_num].pop(0))
    return "".join(result)
    
def get_rail_pattern(length, rails):
    
    pattern = []
    current_rail = 0
    direction = 1
    for _ in range(length):
        pattern.append(current_rail)
        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
        current_rail += direction
    return pattern