from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps
import config

app = Flask(__name__)
# MongoDB connection
client = MongoClient(config.MONGO_URI)
db = client.test_database


@app.route('/users', methods=['POST'])
def create_user():
    # Get request data as JSON
    req_data = request.get_json()
    user = db.user.insert_one(
        {"username": req_data['username'], "email": req_data['email']})
    return dumps({"success": True, "data": user.inserted_id, "message": 'Hello World!'})


@app.route('/users', methods=['GET'])
def get_user():
    users = db.user.find({})
    return dumps({"success": True, "data": users})


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
