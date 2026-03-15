from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():  
    # TODO: Return a welcome message
    return jsonify({"message": "Welcome to our RESTful API"}), 200

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
     # TODO: Return all products or filter by ?category=
     
    category = request.args.get("category")
    
    for product in products:
        if product['category'] == category:
            filtered_by_category = [product]
            return jsonify(filtered_by_category), 200
        
    return jsonify(products), 200 
    

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    # TODO: Return product by ID or 404
    for product in products:
        if product['id'] == id:
            return jsonify(product, 200)
        
    return jsonify({"message": "The product with the id does not exist!"}, 404)

if __name__ == "__main__":
    app.run(debug=True)
