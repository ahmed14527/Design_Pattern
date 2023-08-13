from abc import ABC, abstractmethod

# Abstract Product
class AbstractProduct(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Products
class ConcreteProduct1(AbstractProduct):
    def operation(self):
        print("ConcreteProduct1 operation")

class ConcreteProduct2(AbstractProduct):
    def operation(self):
        print("ConcreteProduct2 operation")

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self) -> AbstractProduct:
        pass

# Concrete Factories
class ConcreteFactory1(AbstractFactory):
    def create_product(self) -> AbstractProduct:
        return ConcreteProduct1()

class ConcreteFactory2(AbstractFactory):
    def create_product(self) -> AbstractProduct:
        return ConcreteProduct2()

# Client code
def client_code(factory: AbstractFactory):
    product = factory.create_product()
    product.operation()

# Usage
factory1 = ConcreteFactory1()
client_code(factory1)

factory2 = ConcreteFactory2()
client_code(factory2)
