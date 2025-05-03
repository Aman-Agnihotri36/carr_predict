from src.jobprediction.config.configuration import ConfigurationManager
from src.jobprediction.components.prediction import Prediction


def PredictionPipeline():
  config=ConfigurationManager()
  prediction_config=config.PredictionManager()
  prediction=Prediction(config=prediction_config)
  prediction.predict()
