class Matrix:
    def __init__(self, matrix_string):
        lines = matrix_string.split("\n")
        self.rows = []
    
        for line in lines:
            row = [int(num) for num in line.split()]
            self.rows.append(row)
            
    def row(self, index):
        
          return list(self.rows[index - 1])

    def column(self, index):
        columns = list(zip(*self.rows))
        return list(columns[index - 1])
