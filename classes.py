class Mypuppy:
  def __init__(self,dogName):
    self.name = dogName

  def bark(self):
      print("woooh!")

my_dog = Mypuppy("Casio")

print(type(my_dog))

my_dog.bark()
print(isinstance(my_dog,Mypuppy))

my_dog = Mypuppy("Rocky")
my_dog2 = Mypuppy("lola")

print(my_dog.name)
print(my_dog2.name)

