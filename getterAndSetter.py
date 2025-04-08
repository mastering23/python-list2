class Puppy:
  def __init__(self, name , age):
    self.__name = name
    self.age = age

  def get_name(self):
    return self.__name

  def set_name(self,name):
    self.__name = name

  def bark(self):
    print(f"{self.__name} bark : Guau!")


  @classmethod
  def factory(cls):
    return cls("Rocky",3)

dog1 = Puppy.factory()
dog1.bark()
# print(dog1.__name)#private

print(dog1.get_name())

print(dog1.__dict__) #dictionary access to all property of the class\
print(dog1._Puppy__name)