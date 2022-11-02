class Gan:
    damage = 10
    strength = 15
    
    def __init__(self, rang):
        if rang == ('C'):
            self.damage += 15
        elif rang == ('B'):
            self.damage += 20
        elif rang == ('A'):
            self.damade += 40
        elif rang == ('S'):
            self.damage += 50





class Person:
    age = 17
    hp = 10
    lvl = 1

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def level_up(self):
        self.damage += 15
        self.hp += 10
        self.lvl += 1
        print("Вы подняли свой lvl, yee")

    def get_item(self, item):
        self.damage += 15



class Elf:
    age = 600
    hp = 1000
    mana = 1000
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def level_up(self):
        self.damage += 15
        self.hp += 10
        self.lvl += 1
        print("Вы подняли свой lvl, yee")

    def get_item(self, item):
        self.damage += 15



Vadim = Person('Вадим', 10)
Aziz = Person('Азиз', 10)


qzibet = Elf('Бекназар', 10000)


Vadim.age = 17
Vadim.hp = 100

Aziz.age = 18
Aziz.damage = 100

gan = Gan('S')
print(f'Имя:{Vadim.name} жизнь:{Vadim.hp} возраст:{Vadim.age} урон: {Vadim.damage}')
print(f'Имя:{qzibet.name} жизнь:{qzibet.hp} возраст:{qzibet.age} урон: {qzibet.damage}')
Vadim.level_up()
Vadim.get_item(gan)
qzibet.get_item(gan)
print(f'Имя:{Vadim.name} жизнь:{Vadim.hp} возраст:{Vadim.age} урон: {Vadim.damage}')
print(f'Имя:{qzibet.name} жизнь:{qzibet.hp} возраст:{qzibet.age} урон: {qzibet.damage}')
