from mlflow_project import logger
from mlflow_project.components.data_transformation import DataTransformation
from mlflow_project.config.configuration import ConfigurationManager

STAGE_NAME_03 = "Data Transformation Pipeline"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the data transformation pipeline if and only if the validation status is True."""
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        # Checks if validation status is True if not don't run the transformation pipeline
        with open(data_transformation_config.status_file_path, "r") as f:
            status = (f.read().split(" ")[-1]) == "True"

        if status:
            logger.info(
                "Schema validation is successful. Proceeding with transformation pipeline"
            )
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
        else:
            raise Exception("Data schema invalid. Transformation pipeline terminated")


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_03} has started")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.forward()
        logger.info(f"{STAGE_NAME_03} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
