class Car:
    car_types = ['sedan', 'suv', 'coupe', 'hatchback', 'truck']

    def __init__(self, brand, model, year, fuel_consumption, car_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_consumption = fuel_consumption
        self.car_type = car_type
        self.is_running = False
        self.mileage = 0
        self.fuel = 0

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print("Двигатель запущен")
        else:
            print("Двигатель уже запущен")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print("Двигатель остановлен")
        else:
            print("Двигатель уже остановлен")

    def get_available_distance(self):
        return self.fuel / self.fuel_consumption * 100

    def drive(self, distance):
        if not self.is_running:
            print("Двигатель не запущен")
            return

        available_distance = self.get_available_distance()
        print(f"Можете проехать {available_distance} км")
        if available_distance < distance:
            print(f"Топливо закочилось. Проехали {available_distance} км")
            self.fuel = 0
            self.is_running = False
            self.mileage += available_distance
        else:
            print(f"Проехали {distance} км")
            self.fuel -= distance * self.fuel_consumption / 100
            self.mileage += distance

    def refuel(self, amount):
        if amount > 0:
            self.fuel += amount
        else:
            print("Невозможное количесто топлива")

    def get_info(self):
        return (f"Марка: {self.brand}. Модель: {self.model}. Год: {self.year}. Тип: {self.car_type}\n"
                f"Расход топлива: {self.fuel_consumption} л на 100 км. Пробег: {self.mileage} км\n"
                f"Топливо: {self.fuel} л")

    @classmethod
    def get_car_types(cls):
        return cls.car_types

    @classmethod
    def from_dict(cls, car_dict):
        return cls(
            brand = car_dict['brand'],
            model = car_dict['model'],
            year = car_dict['year'],
            fuel_consumption = car_dict['fuel_consumption'],
            car_type = car_dict['car_type'],
        )

    @staticmethod
    def calculate_necessary_fuel(distance, fuel_consumption):
        return distance * fuel_consumption

    @staticmethod
    def is_vintage_car(year):
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - year >= 25

car_1 = Car("BMW", "M3", 2015, 4.5, "sedan")
print(car_1.get_info())
car_1.refuel(45)
car_1.start_engine()
car_1.drive(100)
print(car_1.get_info())
