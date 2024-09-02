from api.models import Customer

def customer_resolver(*_, id):
  return Customer.get_customer(id)
