class Car:
    def __init__(self,color, model, age):
        self.color = color
        self.model = model
        self.age = age

Toyota = Car("Синий", "camry xv20", 2008)

print(f'цвет: {Toyota.color}, модель: {Toyota.model}, год выпуска: {Toyota.age}')


class Employee:
    def __init__(self, name, surname, gender, date_birth):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.date_birth = date_birth

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.gender}, {self.date_birth}'

empl = Employee("beks", "tur", "male", "27 april")
empl2 = Employee("kirill", "yora", "gay", "29 february")
        
print(empl)
print(empl2)





class Human:
    def __init__(self, name, age, lesson):
        self.name = name 
        self.age = age
        self.lesson = lesson
    def __str__(self):
        return f'{self.name}, {self.age}, {self.lesson}'

class Teacher(Human):
    def __init__(self, salary, specialty):
        self.salary = salary
        self.specialty = specialty

    def __str__(self):
        return f'{self.salary}, {self.specialty}'

class Student(Human):
    def __init__(self, grade):
        self.grade = grade

    def __str__(self):
        return f'{self.grade}'

Kirill = Human('кирилл', 17, 'матеша')
Gus = Teacher(100, 'препод')
kate = Student(10)

print(Kirill)
print(Gus)
print(kate)

