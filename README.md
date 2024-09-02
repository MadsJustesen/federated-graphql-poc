# Federation POC

This is a small POC to show how federated graphql can work with Apollo router

### Contents

This repository contains a supergrah config file and 3 small python services using Flask and Ariadne:

- Shop
- Products
- Customers

Customers is a plain graphql service, while Shop and Products implements federated schema types

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
