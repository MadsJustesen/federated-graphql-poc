# Federation POC

This is a small POC to show how federated graphql can work with Apollo router.
About federation: https://www.apollographql.com/docs/federation/

### Contents

This repository contains a supergrah config file and 3 small python services using Flask and Ariadne:

- Shop
- Products
- Customers

Customers is a plain graphql service, while Shop and Products implements federated schema types

A shop has products that a api-consumer might want to query. In this example Shop does not resolve a list of products in its own subgraph, but rather sets a list of productIds for that Shop. Via federation, the Product service will resolve the products list on the Shop type, and expose all fields that the Product service has defined on the Product type. The Shop does not know anything about the Product type.

### Prerequisites

To run this project you need:

- python3
- To clone the project
- Inside the project folder, download the router binary: `curl -sSL https://router.apollo.dev/download/nix/latest | sh`
- Install Rover with brew: `brew install rover`

### To run:

There's already a composed supergraph in the repo, but if you want to try and compose it, or if you make changes to the subgraphs, you need to run this command: <br> `rover supergraph compose --config supergraph.yaml --output supergraph.graphql`

Next, start the 3 services in 3 separate terminal windows:

- The expected ports are defined in the supergraph.yaml file, and is the following by default:
  - Customers: port 5000
  - Products: port 5001
  - Shop: port 5002
- To start the flask services, for each one do:
  - `source <service>/bin/activate` to activate venv (python virtual environment)
  - `export FLASK_APP=app.py`
  - `flask run --port=<portnumber>`

In yet another terminal window start router:
`./router --dev --supergraph supergraph.graphql`

After this you can got to http://localhost:4000/ and query the supergraph
