from typing import override

class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        print("Неизвестное передвижение")

class Dog(Animal):
    def __init__(self, breed, price):
        super().__init__(breed, price)

    @override
    def __str__(self):
        return f"Животное {self.breed} {self.price}\n"

class Fish(Animal):
    def __init__(self, breed, price):
        super().__init__(breed, price)

    @override
    def move(self):
        print("Рыба плывет")

    @override
    def __str__(self):
        return f"Рыба {self.breed} {self.price}\n"

class Bird(Animal):
    def __init__(self, name, price):
        super().__init__(name, price)

    @override
    def move(self):
        print("Птица летает")

    @override
    def __str__(self):
        return f"Птица {self.breed} {self.price}\n"

class ZooShop:
    def __init__(self, animals = None):
        if animals is None:
            animals = []
        self.animals = animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_most_expensive_animal(self):
        return max(self.animals, key=lambda animal: animal.price)

    def save_to_file(self):
        with open("Animals.txt", "w", encoding="utf-8") as file:
            for animal in self.animals:
                file.write(animal.__str__())

fish1 = Fish("Порода1", 200)
fish2 = Fish("Порода2", 250)
bird1 = Bird("Порода3", 560)
bird2 = Bird("Порода4", 420)

ZooShop = ZooShop()
ZooShop.add_animal(fish1)
ZooShop.add_animal(fish2)
ZooShop.add_animal(bird1)
ZooShop.add_animal(bird2)
ZooShop.save_to_file()

print(ZooShop.get_most_expensive_animal())