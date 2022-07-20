class Class:
    students = []
    grades = []
    __students_count = 22

    def __init__(self, name):
        self.name = name



    def add_student(self, name: str, grade: float):
        self.name = name
        self.grade = grade
        if len(Class.students) < Class.__students_count:
            Class.students.append(self.name)
            Class.grades.append(self.grade)

    def get_average_grade(self):
        average_grade = sum(Class.grades) / len(Class.grades)

    def __repr__(self):
        return f"The students in {self.name}: {students}. Average grade: {self.average_grade:.2f}"

    a_class = Class("11B")
    a_class.add_student("Peter", 4.80)
    a_class.add_student("George", 6.00)
    a_class.add_student("Amy", 3.50)
    print(a_class)
