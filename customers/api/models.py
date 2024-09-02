class Customer():

  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init__(self, id, name):
    self.id = id
    self.name = name

  def get_customer(id):
    return Customer(id, "Customer" + str(id))

