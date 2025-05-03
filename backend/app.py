import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from jobprediction.components.prediction import PredictionPipeline

from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/predict-career", methods=["POST"])
def predict_career():
    data = request.json
    user_input = data.get("input")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        prediction_result = PredictionPipeline(user_input)
        return jsonify({"prediction": prediction_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
