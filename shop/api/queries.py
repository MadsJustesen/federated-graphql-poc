
from pathlib import Path

from api.models import Shop
from ariadne.contrib.federation import FederatedObjectType, make_federated_schema
from ariadne import ObjectType, load_schema_from_path

query = ObjectType("Query")

@query.field("shop")
def resolve_shop(*_, id: str):
  return Shop.get_shop(id)

shop = FederatedObjectType("Shop")

type_defs = load_schema_from_path(Path(__file__).parent.parent / "schema.graphql")
schema = make_federated_schema(type_defs, query, shop)