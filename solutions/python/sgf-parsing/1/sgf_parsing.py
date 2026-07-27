class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
            
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
                
        for key in other.properties.keys():
            if key not in self.properties:
                return False
                
        if len(self.children) != len(other.children):
            return False
            
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not input_string or input_string[0] != "(":
        raise ValueError("tree missing")
    if input_string[-1] != ")":
        raise ValueError("tree missing")
    if len(input_string) < 3 or input_string[1] != ";":
        raise ValueError("tree with no nodes")
        
    root, _, index = parse_gametree(input_string, 0)
    return root
    
def parse_gametree(s, i):
    i += 1  # skip '('
    root, i = parse_node(s, i)
    last = root
    while s[i] == ";":
        node, i = parse_node(s, i)
        last.children.append(node)
        last = node
    while s[i] == "(":
        child_root, _, i = parse_gametree(s, i)
        last.children.append(child_root)
    i += 1  # skip ')'
    return root, last, i

def parse_node(s, i):
    i += 1  # skip ';'
    properties = {}
    while i < len(s) and s[i].isalpha():
        key, i = parse_key(s, i)
        values, i = parse_values(s, i)
        properties[key] = values
    return SgfTree(properties), i

def parse_key(s, i):
    start = i
    while i < len(s) and s[i].isalpha():
        i += 1
    raw_key = s[start:i]
    if raw_key != raw_key.upper():
        raise ValueError("property must be in uppercase")
    return raw_key, i
    
def parse_values(s, i):
    if i >= len(s) or s[i] != "[":
        raise ValueError("properties without delimiter")
    values = []
    while i < len(s) and s[i] == "[":
        i += 1  # skip '['
        value, i = parse_text(s, i)
        values.append(value)
    return values, i

def parse_text(s, i):
    result = []
    while s[i] != "]":
        if s[i] == "\\":
            next_char = s[i+1]
            if next_char == "\n":
                pass  
            elif next_char.isspace():
                result.append(" ")
            else:
                result.append(next_char)
            i += 2
        elif s[i] == "\n":
            result.append("\n")
            i += 1
        elif s[i].isspace():
            result.append(" ")
            i += 1
        else:
            result.append(s[i])
            i += 1
    i += 1 
    return "".join(result), i