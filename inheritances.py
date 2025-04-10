class Aninal:
  def eat(self):
    print("Eating")

class Dog(Aninal):
  def walk(self):
    print("Walking")
dog = Dog()
dog.eat()


class Rescue_Dog(Dog):

  def findTarget(self):
    print("Found something")
dog = Rescue_Dog()
dog.eat()
dog.walk()
