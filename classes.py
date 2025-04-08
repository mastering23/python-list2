class Mypuppy:
  def __init__(self, dogName):
    self.name = dogName

  @classmethod
  def bark(cls):
    print("Guau!")

  def bark(self):
    print("woooh!")

  @classmethod
  def factory(cls):
    return cls("Happy Rex")



my_dog = Mypuppy("Casio")

print(type(my_dog))
my_dog.bark()
print(isinstance(my_dog, Mypuppy))

my_dog = Mypuppy("Rocky")
my_dog2 = Mypuppy("Lola")

print(my_dog.name)
print(my_dog2.name)

my_dog3 = Mypuppy.factory()
print(my_dog3.name)