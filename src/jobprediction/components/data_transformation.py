from src.jobprediction.entity.config_entity import DataTransformationConfig
import os
import pandas as pd

class DataTransformation:
  def __init__(self, config=DataTransformationConfig):
    self.config=config

  def load_data(self):
    df=pd.read_csv(self.config.raw_data_path)
    return df

  def feature_selection(self):

    df=self.load_data()

    selected_features = [
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
    'Suggested Job Role'
    ]

    df = df[selected_features]
    return df

  def data_transformation(self):
    path=self.config.processed_data_dir
    filename=self.config.processed_data_name
    df=self.feature_selection()
    os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
    filepath = os.path.join(path, filename)
    df.to_csv(filepath, index=False)  # Save the DataFrame to the specified path
