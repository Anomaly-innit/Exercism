class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    custom_words = {}
    
    
    for line in input_data:
        if line.startswith(":"):
            tokens = line.lower().split()
            word_name = tokens[1]
            if word_name.lstrip("-").isdigit():
                    raise ValueError("illegal operation")
            definition = []
            for t in tokens[2:-1]:
                
                if t in custom_words:
                    definition.extend(custom_words[t])  # expand now
                else:
                    definition.append(t)
            custom_words[word_name] = definition
            continue

        
        tokens = line.lower().split()
        i = 0
        while i < len(tokens):
            token = tokens[i]
            i += 1
            if token in custom_words:
                tokens = tokens[:i] + custom_words[token] + tokens[i:]
                
            elif token.lstrip("-").isdigit():
                stack.append(int(token))
                
            elif token == "+" :
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-" :
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*" :
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/" :
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                b = stack.pop()
                a = stack.pop()
                if b == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(a // b)
                    
                
            elif token == "dup" :
                if len(stack) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-1])   
            elif token == "drop" :
                if len(stack) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.pop()
            elif token == "swap" :
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                
                stack[-1], stack[-2] = stack[-2], stack[-1]
                
            elif token == "over" :
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-2])
            else:
                raise ValueError("undefined operation")
            
    return stack