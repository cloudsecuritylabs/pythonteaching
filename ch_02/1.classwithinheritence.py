class Vehicle:

    def __init__(self, wheel = '4', color =' red'):
        self.wheel = wheel
        self.color = color

    def get_wheel(self):
        return self.wheel

    def get_color(self):
        return self.color

    # catching some errors
    # interface -> you can use this to design class interface
    def myprint(self):
        raise NotImplementedError("Not Implemented")

    def total_vehicles(self):
        return 10

    def __str__(self):
        return f'A vehicle is here with {self.wheel} wheels.'

class Bike(Vehicle):
    def get_wheel(self):
        self.wheel = 2
        return 2

    def total_vehicles(self):
        total = super().total_vehicles()
        return total + 1

v = Vehicle()
b= Bike()

print(v.get_wheel())
print(v.wheel)

print(b.get_wheel())
print(b.wheel)
# print(b.myprint()) # uncomment
print(b.total_vehicles())

# super is a keyword that we would only use in a sub class

print(b)