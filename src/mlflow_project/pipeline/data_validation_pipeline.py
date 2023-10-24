from mlflow_project import logger
from mlflow_project.components.data_validation import DataValidation
from mlflow_project.config.configuration import ConfigurationManager

STAGE_NAME_02 = "Data Validation Pipeline"


class DataValidationPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the data validation pipeline."""
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validation_columns()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_02} has started")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.forward()
        logger.info(f"{STAGE_NAME_02} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
