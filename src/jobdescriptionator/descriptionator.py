from src.jobdescriptionator.prompt_builder import get_explanation
from src.jobdescriptionator.profile_formatter import format_profile

def description(predicted_role, profile_raw):
    profile = format_profile(profile_raw)

    predicted_role = predicted_role
    explanation = get_explanation(profile, predicted_role)
    
    print(explanation)
    return explanation

