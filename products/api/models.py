class Product():

  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init__(self, id, name, sku):
    self.id = id
    self.name = name
    self.sku = sku

  def get_product(id):
    return Product(id, "Product_" + str(id), "SKU_ITEM_" + str(id))
  
