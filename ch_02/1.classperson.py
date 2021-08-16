# arributes -> variables inside a class
#           -> usually got self.something
# method is a function inside a class
class Car:
    greeting = "Hello my friend"
    def __init__(self, model='toyota', make = 'camry'):
        self.model = model
        self.make = make

    def promo(self):
        print("promo all year")

    def get_model(self):
        return self.model

    def get_make(self):
        return self.make

my_car = Car()
my_car.promo()