import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.jobprediction.components.prediction import PredictionPipeline
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.jobfinderai.agent import run_agent
from src.jobfinderai.fetch_job import fetch_jobs

app = Flask(__name__)

# Allowing CORS for all origins
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins (you can specify origins as needed)

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
        job_results = fetch_jobs(predicted_role)
        return jsonify({"recommended_jobs": job_results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def fetch_jobs(role: str) -> dict:
    """
    Generates a Google search link for the given job role across multiple platforms like LinkedIn, Indeed, etc.
    """
    # Sanitize the role to make it URL-friendly
    query = f"{role} site:linkedin.com/jobs OR site:indeed.com OR site:unstop.com OR site:glassdoor.com"
    google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    return {"Google_Link": google_search_url}

if __name__ == "__main__":
    app.run(debug=True)
