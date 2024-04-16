import math


class Circle:
    def __init__(self, radius: float):
        assert radius >= 0, f'The radius {radius} is not greater or equal to 0'

        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


radius = int(input('Enter the radius of the circle: '))

circle = Circle(radius)

area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print(f'''
The circle has a radius of {radius}.
> Its area is equal to {area:.2f}
> Its perimeter is equal to {perimeter:.2f}
''')
