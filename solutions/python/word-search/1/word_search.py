DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        for y in range(len(self.puzzle)):
            for x in range(len(self.puzzle[y])):
                for dx, dy in DIRECTIONS:
                    if self._matches(word, x, y, dx, dy):
                        end_x = x + dx * (len(word) - 1)
                        end_y = y + dy * (len(word) - 1)
                        return (Point(x, y), Point(end_x, end_y))
        return None

    
    def _matches(self, word, x, y, dx, dy) :
        for i, letter in enumerate(word):
            nx = x + dx*i
            ny = y + dy*i
            if not (0 <= ny < len(self.puzzle) and 0 <= nx < len(self.puzzle[ny])):
                return False
            if self.puzzle[ny][nx] != letter:
                return False
        return True