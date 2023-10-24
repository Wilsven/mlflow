from mlflow_project import logger
from mlflow_project.components.data_transformation import DataTransformation
from mlflow_project.config.configuration import ConfigurationManager

STAGE_NAME_03 = "Data Transformation Pipeline"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the data transformation pipeline."""
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_03} has started")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.forward()
        logger.info(f"{STAGE_NAME_03} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
