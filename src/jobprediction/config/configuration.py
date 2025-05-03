from src.jobprediction.utils.common import read_yaml_file, create_directory
from src.jobprediction.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainingConfig, PredictionConfig

class ConfigurationManager:
  def __init__(self):
    self.config=read_yaml_file("config/config.yaml")
    self.params=read_yaml_file("params.yaml")
    create_directory(self.config["root"])

  def DataIngestionManager(self):
    config=self.config["data_ingestion"]
    create_directory(config["raw_data_dir"])
    data_ingestion_config=DataIngestionConfig(
        root=config["root"],
        raw_data_dir=config["raw_data_dir"],
        link=config["link"],
        raw_data_name=config["raw_data_name"]
    )
    return data_ingestion_config

  def DataTransformationManager(self):
    config=self.config["data_transformation"]
    create_directory(config["processed_data_dir"])
    data_transformation_config=DataTransformationConfig(
        root=config["root"],
        processed_data_dir=config["processed_data_dir"],
        processed_data_name=config["processed_data_name"],
        raw_data_path=config["raw_data_path"]
    )
    return data_transformation_config

  def ModelTrainingManager(self):
    config=self.config["model_training"]
    params=self.params
    create_directory(config["root"])
    create_directory(config["model_dir"])
    model_training_config=ModelTrainingConfig(
        root=config["root"],
        model_dir=config["model_dir"],
        processed_data_path=config["processed_data_path"],
        model_path=config["model_path"],
        encoder_path=config["encoder_path"],
        scaler_path=config["scaler_path"],
        activation=params["activation"],
        hidden_layer_sizes=params["hidden_layer_sizes"],
        solver=params["solver"],
        report_path=config["report_path"]
    )
    return model_training_config

  def PredictionManager(self):
    config=self.config["prediction"]
    prediction_config=PredictionConfig(
      model_path= config["model_path"],
      encoder_path= config["encoder_path"],
      scaler_path= config["scaler_path"]
    )
    return prediction_config