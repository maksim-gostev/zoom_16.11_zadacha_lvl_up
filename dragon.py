import random


class Dragon:
    def __init__(self, level):
        self.level = level
        self.health = self.calculation_health(level)
        self.is_alive = True
        self.damage = self.calculation_damage(level)
        self.xp = self.calculation_xp(level)

    @classmethod
    def calculation_health(cls, level):
        health = 100
        if level > 1:
            for i in range(level):
                health += health / 2
                if health % 10 > 0:
                    health = (health // 10 + 1) * 10
        return health

    @classmethod
    def calculation_damage(cls, level):
        damage = 10
        for i in range(level):
            damage += damage / 10
        return damage

    @classmethod
    def calculation_xp(cls, level):
        xp = 15
        for i in range(level):
            xp += xp / 5
        return xp

    def bite(self):
        damag = random.randint(1, self.damage)
        return damag

    def get_damage(self, damage):
        self.health -= damage
        self.is_alive = self.die(self.health)

    def get_health(self):
        return self.health

    @classmethod
    def die(cls, hp):
        if hp <= 0:
            return False
        else:
            return True

    def get_xp(self):
        return self.xp

    def get_is_alive(self):
        return self.is_alive