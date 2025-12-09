#Task1
yourName = input("İsim:")
yourAge = int(input("Yaş:"))

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_raw(cls, name_str, age_str):
        name = name_str.strip().title()
        try:
            age = int(age_str)
        except (TypeError, ValueError) as exc:
            raise ValueError("Age must be an integer") from exc
        if age < 0:
            raise ValueError("Age must be non-negative")
        return cls(name, age)
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"
print(Student.from_raw(yourName, yourAge))

#Task2
class Course:
    total_courses = 0
    def __init__(self, title):
        self.title = title
        self.students = []
        Course.total_courses += 1

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Expected a Student")
        self.students.append(student)
    def summary(self):
        return f"{self.title}: {len(self.students)} enrolled | total courses: {Course.total_courses}"
    


