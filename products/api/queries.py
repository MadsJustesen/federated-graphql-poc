from pathlib import Path

from api.models import Product
from ariadne.contrib.federation import FederatedObjectType, make_federated_schema
from ariadne import ObjectType, load_schema_from_path

query = ObjectType("Query")

@query.field("product")
def resolve_product(*_, id: str):
  return Product.get_product(id)

shop = FederatedObjectType("Shop")

@shop.reference_resolver
def resolve_shop_reference(_, _info, representation):
  return {"productIds": representation["productIds"]}

@shop.field("products")
def resolve_shop_products(representation, *_):
  return [Product.get_product(id) for id in representation["productIds"]]


type_defs = load_schema_from_path(Path(__file__).parent.parent / "schema.graphql")
schema = make_federated_schema(type_defs, query, shop)