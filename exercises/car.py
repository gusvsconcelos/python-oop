from datetime import datetime


class Car:
    all = []

    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.__year = year
        self.color = color

        Car.all.append(self)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1886:
            raise Exception('There were no cars before 1886!')
        elif value > datetime.now().year:
            raise Exception('Invalid year.')

        self.__year = value

    def car_age(self):
        today = datetime.now()
        return today.year - self.year

    @staticmethod
    def valid_year(year):
        if year < 1886:
            return False

        return True

    def __repr__(self):
        return f'{self.__class__.__name__}[{
            self.brand}, {self.model}, {self.year}, {self.color}]'


car1 = Car('Volkswagen', 'T-Cross', 2019, 'Red')
print(Car.valid_year(car1.year))
car2 = Car('Chevrolet', 'Trailblazer', 2022, 'Gray')
car3 = Car('Fiat', 'Toro', 2016, 'White')

car3.year = 2020

for car in Car.all:
    print(f'Brand: {car.brand}, Model: {car.model}, Year: {
          car.year}, Color: {car.color}, Age: {car.car_age()}')
