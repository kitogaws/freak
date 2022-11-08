class Food:
    def __init__(self, name, calories, weight):
        self.name = name
        self.calories = calories
        self.weight = weight

    def __str__(self):
        return f'название: {self.name}, калорийность: {self.calories}, масса: {self.weight}'


burger = Food("бургер", "300 ккал", "100 грамм")

print(burger)


class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
        print('I am climbing the tree') 

Perry = Monkey()
Perry.climb()

print (Perry.max_age)
print(Perry.loves_bananas)

Derry = Monkey()
Derry.climb()

print (Derry.max_age)
print(Derry.loves_bananas)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, num):
        self.num = num

    def __str__(self):
        return f'через {self.num} лет, будет {self.age + self.num} лет'

Stive = Person("John", 23, "male")
Stive.calculate_age(27)
print(Stive)

class Rectangle:

    def __init__(self, length, width, height):
        if int(length) < 0 or int(width) < 0 or int(height) < 0:
            raise ValueError() 
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self):
        return self.length * self.width * self.height