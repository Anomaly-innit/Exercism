class School:
    def __init__(self):
        self.students_by_grade = {}
        self.added_log = []
    def add_student(self, name, grade):
        self.students_by_grade.setdefault(grade, [])
        if name in self.roster():
            self.added_log.append(False)
        else:
            self.added_log.append(True)
            self.students_by_grade[grade].append(name)
        

    def roster(self):
        result = []
        for grade in sorted(self.students_by_grade):
            sorted_students_by_grade = sorted(self.students_by_grade[grade])
            result.extend(sorted_students_by_grade)
        
        return result

    def grade(self, grade_number):
        grades = sorted(self.students_by_grade.get(grade_number, []))
        return grades

    def added(self):
        return self.added_log
