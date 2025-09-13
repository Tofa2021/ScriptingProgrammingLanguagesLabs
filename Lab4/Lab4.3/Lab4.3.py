from typing import override

class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        print("Неизвестное передвижение")

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

    def get_most_expensive_breed(self):
        if not self.animals:
            return None

        most_expensive_animal = self.animals[0]
        for animal in self.animals:
            if animal.price > most_expensive_animal.price:
                most_expensive_animal = animal

        return most_expensive_animal

    def save_to_file(self):
        with open("Animals.txt", "w", encoding="utf-8") as file:
            for animal in self.animals:
                file.write(animal.__str__())

animal1 = Fish("Порода1", 200)
animal2 = Fish("Порода2", 250)
animal3 = Bird("Порода3", 560)
animal4 = Bird("Порода4", 420)

ZooShop = ZooShop()
ZooShop.add_animal(animal1)
ZooShop.add_animal(animal2)
ZooShop.add_animal(animal3)
ZooShop.add_animal(animal4)
ZooShop.save_to_file()

print(ZooShop.get_most_expensive_breed())