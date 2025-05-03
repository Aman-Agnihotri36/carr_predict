import os
from src.jobprediction.pipeline.data_ingestion import DataIngestionPipeline
from src.jobprediction.pipeline.data_transformation import DataTransformationPipeline
from src.jobprediction.pipeline.model_training import ModelTrainingPipeline
from src.jobprediction.pipeline.prediction import PredictionPipeline

def complete_run():
  DataIngestionPipeline()
  DataTransformationPipeline()
  ModelTrainingPipeline()
  # PredictionPipeline()
  print("Project Implemetion Done")

complete_run()