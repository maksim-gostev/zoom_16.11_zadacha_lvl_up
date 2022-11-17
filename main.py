class Heroec:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0
        self.lvl = 1
        self.lvl_up = 15

    def add_experience(self, point):
        self.xp += point
        next_lvl = self.lvl
        while self.xp >= self.lvl_up:
            self.xp -= self.lvl_up
            next_lvl += 1
            self.lvl_up *= 2

            self.hp += self.hp / 2
            if self.hp % 10 > 0 :
                self.hp = (self.hp // 10 + 1) * 10
        self.lvl = next_lvl

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
