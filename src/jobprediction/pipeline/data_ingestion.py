from src.jobprediction.config.configuration import ConfigurationManager
from src.jobprediction.components.data_ingestion import DataIngestion


def DataIngestionPipeline():
  config=ConfigurationManager()
  data_ingestion_config=config.DataIngestionManager()
  data_ingestion=DataIngestion(config=data_ingestion_config)
  data_ingestion.download_data()