import random


class Heroes:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0
        self.lvl = 1
        self.lvl_up = 15
        self.damage = 20
        self.is_alive = True

    def add_experience(self, point):
        self.xp += point
        next_lvl = self.lvl
        while self.xp >= self.lvl_up:
            self.xp -= self.lvl_up
            next_lvl += 1
            self.lvl_up *= 2

            self.hp += self.hp / 2
            if self.hp % 10 > 0:
                self.hp = (self.hp // 10 + 1) * 10

            self.damage += self.damage / 5
        self.lvl = next_lvl

    def get_level(self):
        return self.lvl

    def get_health(self):
        return self.hp

    @classmethod
    def die(cls, hp: object) -> object:
        if hp <= 0:
            return False

        else:
            return True


    def bite(self):
        damag = random.randint(1, self.damage)
        return damag

    def get_damage(self, damage):
        self.hp -= damage
        self.is_alive = self.die(self.hp)

    def get_is_alive(self):
        return self.is_alive

    def get_damag_heroes(self):
        return self.damage

    def recovery_hp(self, hp):
        self.hp = hp