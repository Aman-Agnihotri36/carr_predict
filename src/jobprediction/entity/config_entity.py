from dataclasses import dataclass
import os
@dataclass
class DataIngestionConfig:
    root:str
    raw_data_dir:str
    link:str
    raw_data_name:str


@dataclass
class DataTransformationConfig:
  root:str
  processed_data_dir:str
  processed_data_name:str
  raw_data_path:str


@dataclass
class ModelTrainingConfig:
  root:str
  model_dir:str
  processed_data_path:str
  model_path:str
  encoder_path:str
  scaler_path:str
  activation:str
  hidden_layer_sizes:tuple
  solver:str
  report_path:str

@dataclass
class PredictionConfig:
  model_path: str
  encoder_path: str
  scaler_path: str

class PredictionConfig:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # gets /opt/render/project/src/jobprediction
        self.model_path = os.path.join(base_dir, 'artifacts', 'training', 'model', 'job_prediction_model.pkl')
        self.data_path = os.path.join(base_dir, 'artifacts', 'ingestion', 'raw_data', 'roo_data.csv')

        # Optional: print to confirm
        print("Model Path:", self.model_path)
        print("Data Path:", self.data_path)
        
class ConfigurationManager:
    def PredictionManager(self):
        return PredictionConfig()