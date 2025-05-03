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
        # Detect if running on Render
        if os.getenv('RENDER'):
            base_dir = '/opt/render/project/src'
        else:
            # Fallback for local development
            script_dir = os.path.dirname(os.path.abspath(__file__))
            base_dir = os.path.dirname(script_dir)  # Adjust if needed

        # Debug: Log directory and environment details
        print("Base Directory:", base_dir)
        print("Files in Base Directory:", os.listdir(base_dir))
        print("Current Working Directory:", os.getcwd())

        # Construct paths (updated to match repository structure)
        self.model_path = os.getenv(
            'MODEL_PATH',
            os.path.join(base_dir, 'artifacts', 'training', 'model', 'job_prediction_model.pkl')
        )
        self.data_path = os.getenv(
            'DATA_PATH',
            os.path.join(base_dir, 'artifacts', 'ingestion', 'raw_data', 'raw_data.csv')
        )

        # Debug: Log paths and directory contents
        model_dir = os.path.dirname(self.model_path)
        print("Model Path:", self.model_path)
        print("Model Directory Exists:", os.path.exists(model_dir))
        print("Files in Model Directory:", os.listdir(model_dir) if os.path.exists(model_dir) else "Model directory does not exist")
        print("Data Path:", self.data_path)

        # Check file existence
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at: {self.model_path}")
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at: {self.data_path}")

class ConfigurationManager:
    def PredictionManager(self):
        return PredictionConfig()