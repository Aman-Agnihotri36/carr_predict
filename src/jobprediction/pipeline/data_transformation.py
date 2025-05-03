
from src.jobprediction.config.configuration import ConfigurationManager
from src.jobprediction.components.data_transformation import DataTransformation


def DataTransformationPipeline():
  config=ConfigurationManager()
  data_transformation_config=config.DataTransformationManager()
  data_transformation=DataTransformation(config=data_transformation_config)
  data_transformation.data_transformation()