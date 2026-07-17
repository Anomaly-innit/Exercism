
class ConnectGame:
    def __init__(self, board):
        self.grid = []
        for row in board.split("\n"):
            cells = row.strip().split(" ")
            self.grid.append(cells)

    def get_winner(self):
        visited = set()
        for col, item in enumerate(self.grid[0]):
            if item == "O":
                self.dfs(0, col, "O", visited)
        last_row = len(self.grid) - 1
        for col in range(len(self.grid[last_row])):
            if (last_row, col) in visited:
                return "O"

        visited = set()
        for row, r in enumerate(self.grid):
            if r[0] == "X":  
                self.dfs(row, 0, "X", visited)
        
        for row in range(len(self.grid)):
            last_col = len(self.grid[row]) - 1
            if (row, last_col) in visited:
                return "X"

        return ""
    

    def dfs(self, row, col, player, visited):
        if (row, col) in visited:
            return
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[row]):
            return
        if self.grid[row][col] != player:
            return
        visited.add((row, col))
        neighbors = [(row, col-1), (row, col+1), (row-1, col), (row-1, col+1), (row+1, col-1), (row+1, col)]
        for r, c in neighbors:
            self.dfs(r, c, player, visited)
                    