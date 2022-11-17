import random

from dragon import Dragon
from heroes import Heroes

if __name__ == '__main__':

    # создаём героя
    heroes = Heroes('nub')

    # левел героя
    lvl_heroes = heroes.get_level()

    # создаём дракона
    dragon = Dragon(random.randint(1, heroes.get_level()))
    print(f'Появился дракон, у него {dragon.get_health()} здоровья')

    # счётчик раундов
    count = 2

    # цмкл обмена ударами
    while heroes.get_is_alive() and dragon.get_is_alive():
        damag_heroes = heroes.bite()
        print(f'Герой бьёт дракона на {damag_heroes}')
        dragon.get_damage(damag_heroes)
        if dragon.get_is_alive():
            damag_dragon = dragon.bite()
            print(f'Дракон бьёт героя на {damag_dragon}')
            heroes.get_damage(damag_dragon)
            if not heroes.get_is_alive():
                print('Герой погиб')
                break
        else:
            print('Дракон погиб')
            print(f'Герой получил {dragon.get_xp()} опыта')
            heroes.add_experience(dragon.get_xp())

        print(f'Раунд {count}')
        count += 1

    if heroes.get_level() > lvl_heroes:

        print(f'Герой повысил уровень до {heroes.get_level()}')
        print(f'Его здоровье выросло до {heroes.get_health()}, а урон до {heroes.get_damag_heroes()}')




