## import the required packages
from flask import Flask, request, jsonify
from flask-sqlalchemy import SQLAlchemy
from flask-marshmallow import Marshmallow

# inti app
app = Flask(__name__)
# create a route for hellow_world
@app.route("/Hellow world", methods=["GET"])
def get_hellow_world_massage():
    return jsonify({"message": "Hellow world"})

# run the server
if __name__ == "__main__":
    app.run=(debug=True)
