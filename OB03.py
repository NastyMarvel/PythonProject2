class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод make_sound() должен быть реализован в подклассах")

    def eat(self):
        print(f"{self.name} кушает")
class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} чирикает")

class Mammal(Animal):
    def __init__(self, name, age, has_hair=True):
        super().__init__(name, age)
        self.has_hair = has_hair

    def make_sound(self):
        print(f"{self.name} рычит")

class Reptile(Animal):
    def __init__(self, name, age, is_cold_blooded=True):
        super().__init__(name, age)
        self.is_cold_blooded = is_cold_blooded

    def make_sound(self):
        print(f"{self.name} шипит")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
bird = Bird("Птичка", 2)
mammal = Mammal("Собачка", 3)
reptile = Reptile("Змея", 5)

animals = [bird, mammal, reptile]
animal_sound(animals)
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.__class__.__name__}: {animal.name}")

    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.__class__.__name__}: {employee.name}")
class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")
zoo = Zoo()

# Добавляем животных
bird = Bird("Птичка", 2)
mammal = Mammal("Собачка", 3)
reptile = Reptile("Змея", 5)

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Добавляем сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Марина")

zoo.add_employee(keeper)
zoo.add_employee(vet)

# Список животных
zoo.list_animals()

# Список сотрудников
zoo.list_employees()

# Действия сотрудников
keeper.feed_animal(mammal)
vet.heal_animal(bird)
zoo = Zoo()

# Добавляем животных
bird = Bird("Птичка", 2)
mammal = Mammal("Собачка", 3)
reptile = Reptile("Змея", 5)

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Добавляем сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Марина")

zoo.add_employee(keeper)
zoo.add_employee(vet)

# Список животных
zoo.list_animals()

# Список сотрудников
zoo.list_employees()

# Действия сотрудников
keeper.feed_animal(mammal)
vet.heal_animal(bird)
