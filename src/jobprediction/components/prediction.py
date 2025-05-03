# import warnings
# warnings.filterwarnings("ignore")
# import pandas as pd
# import os
# # from src.jobprediction.entity.config_entity import PredictionConfig
# import pickle
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from jobprediction.entity.config_entity import ConfigurationManager


# class Prediction:
#   def __init__(self,config=PredictionConfig):
#     self.config=config

#   def get_user_input(self):
#     """
#     Takes user input with numbered options for each feature.

#     Returns:
#     - List of selected feature values in the correct order.
#     """
#     user_input = []
#     data = pd.read_csv("/content/drive/MyDrive/Dataset/roo_data.csv")
#     feature_columns = [
#     'Acedamic percentage in Operating Systems',
#     'percentage in Algorithms',
#     'Percentage in Programming Concepts',
#     'Percentage in Software Engineering',
#     'Percentage in Computer Networks',
#     'Percentage in Electronics Subjects',
#     'Percentage in Computer Architecture',
#     'Percentage in Mathematics',
#     'Percentage in Communication skills',
#     'Hours working per day',
#     'Logical quotient rating',
#     'hackathons',
#     'coding skills rating',
#     'public speaking points',
#     'certifications',
#     'workshops',
#     'Extra-courses did',
#     'Interested subjects',
#     'interested career area ',
#     'Job/Higher Studies?',
#     ]
    
#     data = data[feature_columns]

#     for feature in feature_columns:
#         unique_values = list(data[feature].dropna().unique())  # Get unique values

#         # Display options
#         print(f"\nSelect a value for {feature}:")
#         for idx, value in enumerate(unique_values, start=1):
#             print(f"{idx}. {value}")

#         # Get valid user selection
#         while True:
#             try:
#                 choice = int(input("Enter the number of your choice: "))
#                 if 1 <= choice <= len(unique_values):
#                     user_input.append(unique_values[choice - 1])
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid number.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

#     return user_input

#   def predict_career(self,user_input):
#       """
#       Predicts career role based on user input.

#       Args:
#       - user_input (list): List of feature values in the same order as dataset.

#       Returns:
#       - Predicted career role (string).
#       """
#        # Load trained model
#       model = pickle.load(open(f"{self.config.model_path}", "rb"))

#       # Load dataset to fit encoders
#       data = pd.read_csv("/content/drive/MyDrive/Dataset/roo_data.csv")
      
#       feature_columns = [
#     'Acedamic percentage in Operating Systems',
#     'percentage in Algorithms',
#     'Percentage in Programming Concepts',
#     'Percentage in Software Engineering',
#     'Percentage in Computer Networks',
#     'Percentage in Electronics Subjects',
#     'Percentage in Computer Architecture',
#     'Percentage in Mathematics',
#     'Percentage in Communication skills',
#     'Hours working per day',
#     'Logical quotient rating',
#     'hackathons',
#     'coding skills rating',
#     'public speaking points',
#     'certifications',
#     'workshops',
#     'Extra-courses did',
#     'Interested subjects',
#     'interested career area ',
#     'Job/Higher Studies?',
#     ] # Extract feature names

#       data = data[feature_columns]
#       # Fit encoders on training data
#       one_hot_encoder = OneHotEncoder(handle_unknown='ignore')
#       one_hot_encoder.fit(data.iloc[:, :])

#       scaler = StandardScaler(with_mean=False)
#       scaler.fit(one_hot_encoder.transform(data.iloc[:, :]))

#       if len(user_input) != len(feature_columns):
#           raise ValueError(f"Expected {len(feature_columns)} features, but got {len(user_input)}.")

#       # Convert input to DataFrame
#       user_df = pd.DataFrame([user_input], columns=feature_columns)

#       # Apply OneHot Encoding
#       user_encoded = one_hot_encoder.transform(user_df)

#       # Apply Standard Scaling
#       user_scaled = scaler.transform(user_encoded)

#       # Predict Career Role
#       prediction = model.predict(user_scaled)

#       return prediction[0]

#   def predict(self):
#     user_input=self.get_user_input()
#     prediction=self.predict_career(user_input)
#     print(f"The Prediction is: {prediction}")


# def PredictionPipeline(input):
#     config = ConfigurationManager()
#     prediction_config = config.PredictionManager()
#     prediction = Prediction(config=prediction_config)
#     result = prediction.predict_career(input)
#     return result




import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import os
import pickle
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from jobprediction.entity.config_entity import PredictionConfig, ConfigurationManager
from jobprediction.entity.config_entity import PredictionConfig, ConfigurationManager

class Prediction:
    def __init__(self, config=PredictionConfig):
        self.config = config

    def predict_career(self, user_input):
        """
        Predicts career role based on user input.

        Args:
            user_input (list): List of feature values in the same order as feature_columns.

        Returns:
            Predicted career role (string).
        """
        # Load trained model
        model = pickle.load(open(self.config.model_path, "rb"))

        # Load dataset to fit encoders
        data = pd.read_csv(self.config.data_path)  # Update to use config

        feature_columns = [
            'Acedamic percentage in Operating Systems',
            'percentage in Algorithms',
            'Percentage in Programming Concepts',
            'Percentage in Software Engineering',
            'Percentage in Computer Networks',
            'Percentage in Electronics Subjects',
            'Percentage in Computer Architecture',
            'Percentage in Mathematics',
            'Percentage in Communication skills',
            'Hours working per day',
            'Logical quotient rating',
            'hackathons',
            'coding skills rating',
            'public speaking points',
            'certifications',
            'workshops',
            'Extra-courses did',
            'Interested subjects',
            'interested career area ',
            'Job/Higher Studies?',
        ]

        data = data[feature_columns]

        # Fit encoders on training data
        one_hot_encoder = OneHotEncoder(handle_unknown='ignore')
        one_hot_encoder.fit(data)

        scaler = StandardScaler(with_mean=False)
        scaler.fit(one_hot_encoder.transform(data))

        if len(user_input) != len(feature_columns):
            raise ValueError(f"Expected {len(feature_columns)} features, but got {len(user_input)}.")

        # Convert input to DataFrame
        user_df = pd.DataFrame([user_input], columns=feature_columns)

        # Apply OneHot Encoding
        user_encoded = one_hot_encoder.transform(user_df)

        # Apply Standard Scaling
        user_scaled = scaler.transform(user_encoded)

        # Predict Career Role
        prediction = model.predict(user_scaled)

        return prediction[0]

def PredictionPipeline(input):
    config = ConfigurationManager()
    prediction_config = config.PredictionManager()
    prediction = Prediction(config=prediction_config)
    result = prediction.predict_career(input)
    return result