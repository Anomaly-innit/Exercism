def convert(input_grid):
        
    DIGITS = {
        (" _ ", "| |", "|_|", "   "): "0",
        ("   ", "  |", "  |", "   "): "1",
        (" _ ", " _|", "|_ ", "   "): "2",
        (" _ ", " _|", " _|", "   "): "3",
        ("   ", "|_|", "  |", "   "): "4",
        (" _ ", "|_ ", " _|", "   "): "5",
        (" _ ", "|_ ", "|_|", "   "): "6",
        (" _ ", "  |", "  |", "   "): "7",
        (" _ ", "|_|", "|_|", "   "): "8",
        (" _ ", "|_|", " _|", "   "): "9"
}
    if len(input_grid) % 4 != 0:
         raise ValueError("Number of input lines is not a multiple of four")
        
    for i, row in enumerate(input_grid):
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three") 
            
    groups = []
    for group_start in range(0, len(input_grid), 4):
        
        four_rows = input_grid[group_start:group_start+4]
        group_digits = ""
        for i in range(0, len(four_rows[0]), 3):
            pattern = (four_rows[0][i:i+3], four_rows[1][i:i+3], 
                       four_rows[2][i:i+3], four_rows[3][i:i+3])
            group_digits += DIGITS.get(pattern, "?")
        groups.append(group_digits)
    return ",".join(groups)
        
        