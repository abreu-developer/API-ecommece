from flask import Blueprint, jsonify




product_routes_bp = Blueprint("products_routs", __name__)

@product_routes_bp.route("/products", methods=['POST'])
def insert_product():
    return jsonify({"message":"produto cadastrado"}),200

@product_routes_bp.route("/products/<product_name>", methods=['GET'])
def get_product(product_name):
    return jsonify({"message":f"produto {product_name}"}),200
