BLACK = 'B'
WHITE = 'W'
NONE = ''
class Board:
    
    def __init__(self, board):
        self.grid = board
        
            
    def territory(self, x, y):
        
        
        if y < 0 or y >= len(self.grid) or x < 0 or x >= len(self.grid[y]):
            raise ValueError("Invalid coordinate")
        if self.grid[y][x] != ' ':
            return (NONE, set())
        
        visited = set()
        territory = set()
        borders = set()
        self.dfs(y, x, visited, territory, borders)
        
        if len(borders) == 1:
            owner = borders.pop()
        else:
            owner = NONE
        return (owner, territory)

    def territories(self):
        result = {BLACK: set(), WHITE: set(), NONE: set()}
        visited = set()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == ' ' and (col, row) not in visited:
                    owner, region = self.territory(col, row)
                    if owner == '':
                        owner = NONE
                    result[owner] |= region
                    visited |= region
        return result
            

    def dfs(self, row, col, visited, territory, borders):
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[row]):
            return
        if (row, col) in visited:
            return
        visited.add((row, col))
        cell = self.grid[row][col]
        if cell == ' ':
            territory.add((col, row))
            self.dfs(row - 1, col, visited, territory, borders)
            self.dfs(row + 1, col, visited, territory, borders)
            self.dfs(row, col - 1, visited, territory, borders)
            self.dfs(row, col + 1, visited, territory, borders)
        else:
            borders.add(cell)