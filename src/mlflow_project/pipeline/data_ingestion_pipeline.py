from mlflow_project import logger
from mlflow_project.components.data_ingestion import DataIngestion
from mlflow_project.config.configuration import ConfigurationManager

STAGE_NAME_01 = "Data Ingestion Pipeline"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the data ingestion pipeline."""
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_01} has started")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.forward()
        logger.info(f"{STAGE_NAME_01} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
