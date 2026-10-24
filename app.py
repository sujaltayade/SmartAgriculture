
from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load trained machine learning models
crop_model_path = "models/crop_model.pkl"
fertilizer_model_path = "models/fertilizer_model.pkl"

crop_model = joblib.load(crop_model_path)
fertilizer_model = joblib.load(fertilizer_model_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend_crop", methods=["POST"])
def recommend_crop():
    try:
        data = request.get_json()

        # Collect soil and weather values
        input_data = pd.DataFrame([{
            "N": float(data["N"]),
            "P": float(data["P"]),
            "K": float(data["K"]),
            "temperature": float(data["temperature"]),
            "humidity": float(data["humidity"]),
            "ph": float(data["ph"]),
            "rainfall": float(data["rainfall"])
        }])

        # Predict the suitable crop
        prediction = crop_model.predict(input_data)[0]

        return jsonify({
            "success": True,
            "recommendation": str(prediction)
        })

    except (ValueError, KeyError, TypeError) as error:
        return jsonify({
            "success": False,
            "message": "Please enter valid values in all crop fields."
        }), 400


@app.route("/recommend_fertilizer", methods=["POST"])
def recommend_fertilizer():
    try:
        data = request.get_json()

        # Collect soil, crop and weather values
        input_data = pd.DataFrame([{
            "Temparature": float(data["temperature"]),
            "Humidity": float(data["humidity"]),
            "Moisture": float(data["moisture"]),
            "Soil Type": data["soil_type"],
            "Crop Type": data["crop_type"],
            "Nitrogen": float(data["nitrogen"]),
            "Potassium": float(data["potassium"]),
            "Phosphorous": float(data["phosphorous"])
        }])

        # Predict the fertilizer
        prediction = fertilizer_model.predict(input_data)[0]

        return jsonify({
            "success": True,
            "recommendation": str(prediction)
        })

    except (ValueError, KeyError, TypeError) as error:
        return jsonify({
            "success": False,
            "message": "Please enter valid values in all fertilizer fields."
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
