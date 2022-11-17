class Heroec:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0
        self.lvl = 1
        self.lvl_up = 15

    def add_experience(self, point):
        self.xp += point
        count_hp = 1
        count_lvl = 1
        next_lvl = self.lvl
        while self.xp > 0:
            self.xp -= self.lvl_up
            next_lvl += 1
            self.lvl_up *= 2
            print(f'итерация lvl {count_lvl}')
            count_lvl += 1

        for i in range(next_lvl - self.lvl):
            print(f'итерация hp {count_hp}')
            count_hp += 1
            self.hp += self.hp / 2
            if self.hp % 10 > 0 :
                self.hp = (self.hp // 10 + 1) * 10
        self.lvl = next_lvl
        print(f'test {self.lvl}')

    def get_level(self):
        return f'левел {self.lvl}'

    def get_health(self):
        return f'здоровье {self.hp}'


a = Heroec('нуб')
a.add_experience(60)
print(a.get_level())
print(a.get_health())
a.add_experience(60)
print(a.get_health())
print(a.get_level())
a.add_experience(200)