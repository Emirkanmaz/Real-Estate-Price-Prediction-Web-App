from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/predict_home_price", methods=['GET', "POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bath = int(request.form["bath"])
    balcony = int(request.form["balcony"])
    room = int(request.form["room"])

    response = jsonify({
        "estimated_price": util.get_estimated_price(location,total_sqft,bath,balcony,room)
    })
    return response


if  __name__ == "__main__":
    print("Starting Python Flask Server")
    util.load_saved_artifacts()
    app.run()
