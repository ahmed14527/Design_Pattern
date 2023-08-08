# Prototype base class
class Prototype:
  def clone(self):
    pass

# Concrete prototype classes 
class ConcretePrototype1(Prototype):
  def __init__(self):
    self.attr1 = 'value1'
  
  def clone(self):
    return ConcretePrototype1()

class ConcretePrototype2(Prototype):
  def __init__(self):
    self.attr2 = 'value2'

  def clone(self):
    return ConcretePrototype2()

# Client code
prototype1 = ConcretePrototype1()
prototype2 = ConcretePrototype2()

clone1 = prototype1.clone()
clone2 = prototype2.clone()

print(clone1.attr1)
print(clone2.attr2)
