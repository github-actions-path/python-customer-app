from flask import Flask, jsonify
import json


app = Flask(__name__) 
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
customers = [
    {'id': 0,
        'name': 'John Doe',
        'address': '123 Main St',
        'city': 'San Francisco',
        'state': 'CA',
        'zip': '94101',
        'phone': '415-555-5555',
        'email': 'jdoe@bullshit.gmail'
    }]

@app.route('/customers', methods=['GET'])
def home():
    return jsonify(customers)

app.run(port=5000, debug=True)