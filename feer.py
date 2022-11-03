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


