import gdown
from src.jobprediction.entity.config_entity import DataIngestionConfig
import os
class DataIngestion:
  def __init__(self,config=DataIngestionConfig):
    self.config=config

  def download_data(self):
        if self.config.link:
            file_id = self.config.link.split('/')[-2]
            destination_path = os.path.join(self.config.raw_data_dir, self.config.raw_data_name)
            gdown.download(id=file_id, output=destination_path, quiet=False)
            print(f"Downloaded data to {destination_path}")
        else:
            print("No download link provided.")