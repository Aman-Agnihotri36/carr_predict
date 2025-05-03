from src.jobprediction.config.configuration import ConfigurationManager
from src.jobprediction.components.model_training import ModelTraining


def ModelTrainingPipeline():
  config=ConfigurationManager()
  model_training_config=config.ModelTrainingManager()
  model_training=ModelTraining(config=model_training_config)
  model_training.training()
