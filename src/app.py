"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    new_member = {
        "name": data.get("first_name"),
        "age": data.get("age"),
        "lucky_numbers": data.get("lucky_numbers", [])
    }

    jackson_family.add_member(new_member)

    return jsonify({"message": "Member added successfully"}), 200


@app.route('/member/<int:member_id>', methods=['GET'])
def single_member(member_id):
    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(member_id)
    response_body = {
        "family_member": member
    }
    return jsonify(response_body), 200


@app.route('/member/<int:id>', methods=['PUT'])
def update_member_by_id(id):
    data = request.json

    success = jackson_family.update_member(id, data)
    if success:
        return jsonify({"message": "Member updated successfully"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404
    

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member_by_id(id):
    success = jackson_family.delete_member(id)
    if success:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404


@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

# this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
