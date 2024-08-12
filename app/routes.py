from flask import Blueprint, jsonify
from .data_store import store_data, get_stored_data

main = Blueprint('main', __name__)

# Mock data
mock_data = {
    "orders": [
        {"id": 1, "name": "Product 1", "quantity": 5},
        {"id": 2, "name": "Product 2", "quantity": 10}
    ]
}

@main.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulate data fetching from an external service
    processed_data = process_data(mock_data)
    store_data(processed_data)
    return jsonify({"message": "Data fetched and processed successfully"}), 200

def process_data(data):
    # Example of data processing: Convert all product names to uppercase
    for order in data["orders"]:
        order["name"] = order["name"].upper()
    return data

@main.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Retrieve processed data from in-memory storage
    data = get_stored_data()
    return jsonify(data), 200
