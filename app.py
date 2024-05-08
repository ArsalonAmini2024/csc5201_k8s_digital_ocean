from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields

# Initialize Flask app and Swagger 
app = Flask(__name__)
api = Api(app, version='1.0', title='Cart API',
          description='A simple API to manage shopping cart items by Arsalon')

# In-memory storage for cart items - to keep it simple and not add external DB 
cart = {}

# Defining the model used in Swagger docs
item_model = api.model('Item', {
    'id': fields.Integer(required=True, description='Item ID'),
    'name': fields.String(required=True, description='Item Name'),
    'quantity': fields.Integer(required=True, description='Quantity'),
    'price': fields.Float(required=True, description='Item Price')
})

# Init a Namespace to organize RESTful endpoints in Swagger UI
ns = api.namespace('cart', description='Cart operations')

# Handle the collection of cart items
@ns.route('/')
class CartCollection(Resource):
    @ns.marshal_with(item_model, as_list=True)
    def get(self):
        """Retrieve all cart items"""
        return list(cart.values())

    @ns.expect(item_model)
    def post(self):
        """Add a new item to the cart"""
        data = request.json
        item_id = data.get('id')
        if item_id is None or item_id in cart:
            api.abort(400, 'Invalid or duplicate item ID')
        cart[item_id] = {
            'id': item_id,
            'name': data['name'],
            'quantity': data['quantity'],
            'price': data['price']
        }
        return {'message': 'Item added', 'item': cart[item_id]}, 201

# Gandle individual cart items by ID
@ns.route('/<int:item_id>')
@ns.response(404, 'Item not found')
@ns.param('item_id', 'The item identifier')
class CartItem(Resource):
    @ns.marshal_with(item_model)
    def get(self, item_id):
        """Retrieve a specific cart item by ID"""
        item = cart.get(item_id)
        if item is None:
            api.abort(404, 'Item not found')
        return item

    @ns.expect({'quantity': fields.Integer})
    def patch(self, item_id):
        """Update the quantity of an existing item"""
        if item_id not in cart:
            api.abort(404, 'Item not found')
        data = request.json
        quantity = data.get('quantity')
        if quantity is not None:
            cart[item_id]['quantity'] = quantity
        return {'message': 'Item updated', 'item': cart[item_id]}

    def delete(self, item_id):
        """Remove an item from the cart"""
        if item_id not in cart:
            api.abort(404, 'Item not found')
        deleted_item = cart.pop(item_id)
        return {'message': 'Item deleted', 'item': deleted_item}

# Register the namespace
api.add_namespace(ns)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

