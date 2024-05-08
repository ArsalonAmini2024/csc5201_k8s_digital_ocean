CSC 5201 Flask Application by Arsalon Amini

The simple flask app has teh following RESTful endpoints:

GET: Retrieve all items or a single item.
POST: Add a new item to the cart.
PATCH: Update the quantity of an existing item.
DELETE: Remove an item from the cart.

Running outside a container: 

- Download the github repo
- create a python env
- download the dependencies flask flask-restx
- Once the app is running, Swagger UI will be available at http://127.0.0.1:5000/.

Running in a container: 

- Download the image from https://hub.docker.com/repository/docker/arsalon/flask-cart-api/general
- Alt - download the docker file in the repo and build the image locally 
