def grep(pattern, flags, files):
    matched_files = ""
    result = ""
    for filename in files:
        with open(filename) as f:
            i = 0
            for line in f:
                i += 1
                stripped_line = line.rstrip("\n")
                if line_matches(stripped_line, pattern, flags):
                    if filename not in matched_files:
                        matched_files += filename + "\n"
                    output = stripped_line
                    if "-n" in flags:
                        output = f"{i}:{output}"
                    if len(files) > 1:
                        output = f"{filename}:{output}"
                    result += output + "\n"
    
    if "-l" in flags:
        return matched_files
    return result
            

def line_matches(line, pattern, flags):
    check_line = line
    check_pattern = pattern
    if "-i" in flags:
        check_line = line.lower()
        check_pattern = pattern.lower()
    
    if "-x" in flags:
        result = check_line == check_pattern
    else:
        result = check_pattern in check_line
    
    if "-v" in flags:
        result = not result
    
    return result
        