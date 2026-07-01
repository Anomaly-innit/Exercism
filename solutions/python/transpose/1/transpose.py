def transpose(text):
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    rows = []
    for i in range(max_len):
        row = ""
        for line_index, line in enumerate(lines):
            if i >= len(line):
                if any(len(other_line) > i for other_line in lines[line_index+1:]):
                    row += " "
                else:
                    row += ""
            else:
                 row += line[i]
                
        rows.append(row)
    return "\n".join(rows)