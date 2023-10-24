from mlflow_project import logger
from mlflow_project.pipeline.data_ingestion_pipeline import (
    STAGE_NAME_01,
    DataIngestionPipeline,
)


try:
    logger.info(f"{STAGE_NAME_01} has started")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.forward()
    logger.info(f"{STAGE_NAME_01} has completed")
except Exception as e:
    logger.exception(e)
    raise e
