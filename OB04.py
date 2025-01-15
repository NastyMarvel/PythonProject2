from abc import ABC, abstractmethod


# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные реализации оружия
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")


class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")


# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def set_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self, monster):
        if self.weapon is not None:
            self.weapon.attack()
            print(f"{monster.name} побеждён!")
        else:
            print("У бойца нет оружия.")


# Шаг 4: Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name


# Основной сценарий игры
def main():
    # Создание бойца и монстров
    fighter = Fighter("Воин")
    monster = Monster("Гоблин")

    # Выбор оружия
    sword = Sword()
    bow = Bow()

    # Бои
    print("\nБоец выбирает меч.")
    fighter.set_weapon(sword)
    fighter.fight(monster)

    print("\nБоец выбирает лук.")
    fighter.set_weapon(bow)
    fighter.fight(monster)


if __name__ == "__main__":
    main()
