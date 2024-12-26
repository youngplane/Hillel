class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {super().__str__()}, Record Book: {self.record_book}"


class GroupLimitError(Exception):
    def __init__(self, message="Група вмещает не более 10 студентов"):
        super().__init__(message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\nStudents:\n{all_students}"


# test
try:
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
    st4 = Student('Female', 24, 'Jane', 'Smith', 'AN147')
    st5 = Student('Male', 34, 'Bill', 'Gates', 'AN148')
    st6 = Student('Female', 18, 'Ann', 'Lee', 'AN149')
    st7 = Student('Male', 36, 'Tom', 'Cruise', 'AN150')
    st8 = Student('Female', 41, 'Emma', 'Watson', 'AN151')
    st9 = Student('Male', 72, 'Chris', 'Evans', 'AN152')
    st10 = Student('Female', 55, 'Scarlett', 'Johansson', 'AN153')
    st11 = Student('Male', 44, 'Robert', 'Downey', 'AN154')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)

    print(gr)

    # Попытка добавить 11-го студента
    gr.add_student(st11)

except GroupLimitError as e:
    print(f"Ошибка: {e}")
