class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def say_my_name(self):
        return f'здраствуйте, меня зовут {self.name}'


class Student(Person):
    def __init__(self, grades):
        self.__grades = grades

    def __str__(self):
        return self.__grades

    def show_grades(self):
        return self.__grades



# class Teacher(Person):
#     def __init__(self):
#         pass

#     def __str__(self):


person = Person("Kirill", 16)
student = Student(100)
student.show_grades()

print(student.show_grades)