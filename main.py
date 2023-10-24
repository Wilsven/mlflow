from mlflow_project import logger
from mlflow_project.pipeline.data_ingestion_pipeline import (
    STAGE_NAME_01,
    DataIngestionPipeline,
)
from mlflow_project.pipeline.data_validation_pipeline import (
    STAGE_NAME_02,
    DataValidationPipeline,
)

try:
    # Data Ingestion Pipeline
    logger.info(f"{STAGE_NAME_01} has started")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.forward()
    logger.info(f"{STAGE_NAME_01} has completed")

    # Data Validation Pipeline
    logger.info(f"{STAGE_NAME_02} has started")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.forward()
    logger.info(f"{STAGE_NAME_02} has completed")
except Exception as e:
    logger.exception(e)
    raise e
