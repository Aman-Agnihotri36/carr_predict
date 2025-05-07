import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.jobprediction.components.prediction import PredictionPipeline


from flask import Flask, request, jsonify
from flask_cors import CORS
from src.jobfinderai.agent import run_agent
from src.jobfinderai.fetch_job import fetch_jobs


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
    
@app.route("/recommended-jobs", methods=["POST"])
def recommended_jobs():
    data = request.json
    predicted_role = data.get("role")

    if not predicted_role:
        return jsonify({"error": "No role provided"}), 400

    try:
        job_results = jobs_recommended(predicted_role)
        return jsonify({"recommended_jobs": job_results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def jobs_recommended(predicted_role: str):
    job_results = run_agent(predicted_role)
    print("\n📄 Recommended Jobs:\n", job_results)
    return job_results

if __name__ == "__main__":
    app.run(debug=True)
