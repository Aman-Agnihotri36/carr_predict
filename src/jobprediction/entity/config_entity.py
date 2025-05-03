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
        base_dir = os.path.dirname(__file__)  # directory of current file
        
        # Use relative paths
        self.data_path = os.path.join(base_dir, '..', 'artifacts', 'ingestion', 'raw_data', 'roo_data.csv')
        self.model_path = os.path.join(base_dir, '..', 'artifacts', 'training', 'model', 'job_prediction_model.pkl')
        
        # Convert to absolute paths for safety
        self.data_path = os.path.abspath(self.data_path)
        self.model_path = os.path.abspath(self.model_path)
        
class ConfigurationManager:
    def PredictionManager(self):
        return PredictionConfig()