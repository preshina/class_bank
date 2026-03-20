# Create a class Student with:

# name, marks

# method to calculate average

# method to display result (pass/fail).

class Student:
    def __init__(self, name, *marks):
        self.name = name
        self.marks = marks

    def calc_average(self):
        marks = self.marks
        total_marks = sum(marks)
        length = len(marks)
        avg = total_marks/length
        return avg

    def result(self):
        if self.calc_average() > 30:
            return "pass"

        else:
            return "fail"


d1 = Student("hari", 20, 30, 40, 20)
d2 = Student("gita", 30, 40, 50, 60)
print(d2.result())
print(d1.calc_average())
print(d1.result())
print(d2.calc_average())
