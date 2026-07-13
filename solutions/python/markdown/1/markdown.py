import re

def parse_header(line):
    match = re.match(r'(#{1,6}) (.*)', line)
    if match:
        level = len(match.group(1))
        content = match.group(2)
        return f'<h{level}>{content}</h{level}>'
    return None

def parse_bold(text):
    match = re.match(r'(.*)__(.*)__(.*)', text)
    if match:
        return match.group(1) + '<strong>' + match.group(2) + '</strong>' + match.group(3)
    return text
    
def parse_italic(text):
    match = re.match(r'(.*)_(.*)_(.*)', text)
    if match:
        return match.group(1) + '<em>' + match.group(2) + '</em>' + match.group(3)
    return text
    
def parse_list_item(line):
    match = re.match(r'\* (.*)', line)
    if match:
        content = match.group(1)
        content = parse_bold(content)
        content = parse_italic(content)
        return '<li>' + content + '</li>'
    return None
                    
def parse(markdown):
    lines = markdown.split('\n')
    result = ''
    in_list = False
    for line in lines:
        header = parse_header(line)
        list_item = parse_list_item(line)
        if header:
            if in_list:
                result += '</ul>'
                in_list = False
            result += header
        elif list_item:
            if not in_list:
                result += '<ul>'
                in_list = True
            result += list_item
        else:
            if in_list:
                result += '</ul>'
                in_list = False
            content = parse_bold(line)
            content = parse_italic(content)
            result += '<p>' + content + '</p>'
    if in_list:
        result += '</ul>'
    return result
    
