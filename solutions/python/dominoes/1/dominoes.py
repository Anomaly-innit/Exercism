def can_chain(dominoes):
    if dominoes == []:
        return dominoes
        
    def backtrack(remaining, current_chain):
        if not remaining:
            if current_chain[0][0] == current_chain[-1][1]:
                return current_chain
            return None
            
            
    
        
        for i, domino in enumerate(remaining):
            
            for oriented in [domino, [domino[1], domino[0]]]:
                
                if not current_chain or current_chain[-1][1] == oriented[0]:
                    current_chain.append(oriented)
                    new_remaining = remaining[:i] + remaining[i+1:]
                    result = backtrack(new_remaining, current_chain)
                
                    if result:
                        return result
                    current_chain.pop()
            
    return backtrack(dominoes, [])
