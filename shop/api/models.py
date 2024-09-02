class Shop():

  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init__(self, id, name, productIds):
    self.id = id
    self.name = name
    self.productIds = productIds

  def get_shop(id):
    return Shop(id, "Shop" + str(id), ["123abc", "234xyz", "332211"])
  
