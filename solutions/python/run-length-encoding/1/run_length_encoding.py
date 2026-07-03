def decode(string):
    result = ""
    i = 0
    while i < len(string):
        if string[i].isdigit():
            
            num_str = ""
            while string[i].isdigit():
                num_str += string[i]
                i += 1
            count = int(num_str)
            char = string[i]
            result += char * count
            i += 1
        else:
            result += string[i]
            i += 1
    return result
        


def encode(string):
    result = ""
    i = 0
    while i < len(string):
        char = string[i]
        count = 1
        while i + count < len(string) and string[i + count] == char:
            count += 1
        if count ==1:
            result += char
        else:
            result += str(count) + char
        i += count
    return result