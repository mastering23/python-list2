class Product:
  def __init__(self,name,price):
    self.name = name
    self.price = price

  def __str__(self):
    return f"Producto: {self.name} - Price : {self.price}"

class Category:
  products = []

  def __init__(self,name,product):
    self.name = name
    self.products = product

  def add(self,product):
    self.products.append(product)

  def viewProduct(self):
    for product in  self.products:
      print(product)

kayak = Product("Kayak",1000)
bat = Product("Wood bat",500)
Surfboard = Product("Suftboard",1500)
sport = Category("Sport",[kayak,bat])
sport.add(Surfboard)
sport.viewProduct()