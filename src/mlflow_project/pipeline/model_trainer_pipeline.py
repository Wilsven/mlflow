from mlflow_project import logger
from mlflow_project.components.model_trainer import ModelTrainer
from mlflow_project.config.configuration import ConfigurationManager

STAGE_NAME_04 = "Model Training Pipeline"


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the model training pipeline."""
        config_manager = ConfigurationManager()
        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_04} has started")
        model_trainer_pipeline = ModelTrainerPipeline()
        model_trainer_pipeline.forward()
        logger.info(f"{STAGE_NAME_04} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
