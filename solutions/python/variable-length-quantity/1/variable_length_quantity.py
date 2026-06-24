def encode(numbers):
    result = []
    for number in numbers:
        chunks = []
        if number == 0:
            chunks = [0]   
        while number > 0:
            chunks.append(number&127)
            number = number>>7
        chunks.reverse()
        for i in range(len(chunks) - 1): 
            chunks[i] = chunks[i] | 128
        result.extend(chunks)
    return result
    
def decode(bytes_):
    
    current = 0
    finale = []
    incomplete = False
    for byte in bytes_:
        incomplete = (byte & 128 != 0)  # True if top bit set, False if clear
        current = (current << 7) | (byte & 127)
        if byte & 128 == 0:
            finale.append(current)
            current = 0
    
    if incomplete:
        raise ValueError("incomplete sequence")
    return finale
    
        
