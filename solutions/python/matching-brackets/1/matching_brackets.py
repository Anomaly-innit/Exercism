def is_paired(input_string):
    stack= []
    openers = ["(","[","{"]
    closing = [")","]","}"]
    matching = {")": "(", "]": "[", "}": "{"}
    for i, something in enumerate(input_string):
        if something in openers:
            stack.append(something)
        elif something in closing:
            if stack == []:
                return False
            if stack[-1] == matching[something]:
                stack.pop(-1)
            else:
                return False
    return stack == []
            
