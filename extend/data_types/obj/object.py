class Car:
    init_quantity = 0
    init_name = 'Toyota'
    def __init__(self, name = init_name):
        self.name = name
        self.quantity = self.init_quantity

    def upvote(self):
        self.quantity += 1

    def move(self):
        print("Moving")

    def stop(self):
        print("Stopping")

    def reset_votes(self):
        self.quantity = Car.init_quantity

    def __str__(self):
        return f"Car: {self.name} - {self.quantity}"
    
    # def __repr__(self):
    #     return f"Car: {self.name} - {self.quantity}"

    def __add__(self, other):
        return (f"Total quantity: {self.quantity + other.quantity}, Total name: {self.name + other.name}")
    
    @staticmethod
    def get_name():
        return 'Toyota'
        
my_car = Car("VW")
my_car.upvote()
print('name:', my_car.name)
print('quantity:', my_car.quantity)
print(my_car)
print(dir(my_car))
print(id(my_car))
print('=================')
print(my_car.__dict__)
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))

my_car2 = Car()
print(id(my_car2))
Car.move(my_car2)
my_car.move()
my_car.stop()

print(Car.get_name())
print(my_car.get_name())

print(my_car)
print(my_car.__repr__())

print(my_car.__str__())
my_car2.upvote()
my_car2.upvote()

print(my_car + my_car2)

print('subclass')

class Truck(Car):
    def __init__(self, name = Car.init_name):
        super().__init__(name)
        self.power = 100
        
my_truck = Truck()
print(my_truck.__dict__)

print(Car.__subclasses__())
