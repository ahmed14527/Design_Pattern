import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.copy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj


class Car:
    def __init__(self):
        self.name = "Default"
        self.color = "Default"
        self.price = 0

    def __str__(self):
        return f"{self.name} | Color: {self.color} | Price: {self.price}"


# Create a prototype instance
prototype = Prototype()

# Create a car object and register it in the prototype
car = Car()
car.name = "Sedan"
car.color = "Red"
car.price = 20000
prototype.register_object("sedan", car)

# Clone the car object using shallow copy and update the price
cloned_car = prototype.clone("sedan")
cloned_car.price = 25000

# Clone the car object using deep copy and update the color
deep_cloned_car = prototype.clone("sedan")
deep_cloned_car.color = "Blue"

# Output the original car and the cloned cars
print("Original Car:", car)
print("Cloned Car (Shallow Copy):", cloned_car)
print("Deep Cloned Car (Deep Copy):", deep_cloned_car)
