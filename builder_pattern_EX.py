class Car:
    def __init__(self):
        self.model = None
        self.engine = None
        self.transmission = None
        self.wheel = None

    def __str__(self):
        return f'Model: {self.model}, Engine: {self.engine}, Transmission: {self.transmission}, Wheels: {self.wheel}'


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_transmission(self, transmission):
        self.car.transmission = transmission
        return self

    def set_wheel(self, wheel):
        self.car.wheel = wheel
        return self

    def build(self):
        return self.car


builder = CarBuilder()
car = builder.set_model('Honda Civic') \
    .set_engine('2.0L') \
    .set_transmission('Automatic') \
    .set_wheel('Alloy Wheels') \
    .build()

print(car)
