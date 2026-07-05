DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
PLANTS = {"G": "grass", "C": "clover", "R": "radishes", "V": "violets"}

class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.students = sorted(students) 
        self.diagram = diagram
        diag_split = self.diagram.split("\n")
        self.diag_split = diag_split
        
    def plants(self, name):
        letters = ""
        result =[]
        index = self.students.index(name)
        letters += self.diag_split[0][index*2 : index*2+2]
        letters += self.diag_split[1][index*2 : index*2+2]
        for letter in letters:
            result.append(PLANTS[letter])
        capitalized_result = []
        for word in result:
            capitalized_result.append(word.title())
        return capitalized_result
        