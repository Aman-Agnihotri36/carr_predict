# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from src.jobprediction.components.prediction import PredictionPipeline
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from src.jobfinderai.agent import run_agent
# from src.jobfinderai.fetch_job import fetch_jobs
# from src.jobdescriptionator.prompt_builder import get_explanation
# from src.jobdescriptionator.profile_formatter import format_profile

# app = Flask(__name__)

# CORS(app, resources={r"/*": {"origins": "*"}})  

# @app.route("/predict-career", methods=["POST"])
# def predict_career():
#     data = request.json
#     user_input = data.get("input")

#     if not user_input:
#         return jsonify({"error": "No input provided"}), 400

#     try:
#         prediction_result = PredictionPipeline(user_input)
#         return jsonify({"prediction": prediction_result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# @app.route("/recommended-jobs", methods=["POST"])
# def recommended_jobs():
#     data = request.json
#     predicted_role = data.get("role")

#     if not predicted_role:
#         return jsonify({"error": "No role provided"}), 400

#     try:
#         job_results = fetch_jobs(predicted_role)
#         return jsonify({"recommended_jobs": job_results})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# def fetch_jobs(role: str) -> dict:
#     """
#     Generates a Google search link for the given job role across multiple platforms like LinkedIn, Indeed, etc.
#     """

#     query = f"{role} site:linkedin.com/jobs OR site:indeed.com OR site:unstop.com OR site:glassdoor.com"
#     google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
#     return {"Google_Link": google_search_url}

# @app.route("/get_description", methods=["POST"])
# def job_description():
#     data = request.json
#     user_role = data.get("role")
#     user_data = data.get("data")

#     if not user_role:
#         return jsonify({"error": "No input provided"}), 400

#     try:
#         prediction_result = description(user_role, user_data)
#         return jsonify({"prediction": prediction_result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# def description(predicted_role, profile_raw):
#     profile = format_profile(profile_raw)

#     predicted_role = predicted_role
#     explanation = get_explanation(profile, predicted_role)
    
#     print(explanation)
#     return explanation



# if __name__ == "__main__":
#     app.run(debug=True)




import sys
import os
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.jobprediction.components.prediction import PredictionPipeline
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.jobfinderai.agent import run_agent
from src.jobfinderai.fetch_job import fetch_jobs
from src.jobdescriptionator.prompt_builder import get_explanation
from src.jobdescriptionator.profile_formatter import format_profile

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

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
    query = f"{role} site:linkedin.com/jobs OR site:indeed.com OR site:unstop.com OR site:glassdoor.com"
    google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    return {"Google_Link": google_search_url}

@app.route("/get_description", methods=["POST"])
def job_description():
    data = request.json
    user_role = data.get("role")
    user_data = data.get("data")

    if not user_role:
        return jsonify({"error": "No input provided"}), 400

    try:
        prediction_result = description(user_role, user_data)
        return jsonify({"prediction": prediction_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def description(predicted_role, profile_raw):
    profile = format_profile(profile_raw)
    explanation = get_explanation(profile, predicted_role)
    print(explanation)
    return explanation

# Scheduler to ping endpoint every 14 minutes
def ping_myself():
    try:
        response = requests.get("http://127.0.0.1:5000/")  # You can change to your deployed URL
        print(f"[{time.ctime()}] Pinged with status {response.status_code}")
    except Exception as e:
        print(f"[{time.ctime()}] Error pinging: {e}")

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=ping_myself, trigger="interval", minutes=14)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    print("Scheduler started. Running Flask app...")
    app.run(debug=True)
