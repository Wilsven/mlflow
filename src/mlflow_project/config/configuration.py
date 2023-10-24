import os

from mlflow_project import logger
from mlflow_project.constants import *
from mlflow_project.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
)
from mlflow_project.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH,
        schema_file_path: Path = SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Creates the root directory and returns
        the configuration for data ingestion.

        Returns:
            DataIngestionConfig: Configuration for data ingestion.
        """
        data_ingestion = self.config.data_ingestion

        create_directories([data_ingestion.root_dir])

        file_path = os.path.join(data_ingestion.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {data_ingestion.root_dir}"
                )
                pass

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(data_ingestion.root_dir),
            source_url=str(data_ingestion.source_url),
            local_data_file=Path(data_ingestion.local_data_file),
            unzip_dir=Path(data_ingestion.unzip_dir),
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Creates the root directory and returns
        the configuration for data validation.

        Returns:
            DataValidationConfig: Configuration for data validation.
        """
        data_validation = self.config.data_validation
        schema = self.schema.columns

        create_directories([data_validation.root_dir])

        file_path = os.path.join(data_validation.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {data_validation.root_dir}"
                )
                pass

        data_validation_config = DataValidationConfig(
            root_dir=Path(data_validation.root_dir),
            unzip_data_path=Path(data_validation.unzip_data_path),
            status_file_path=Path(data_validation.status_file_path),
            data_schema=dict(schema),
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Creates the root directory and returns
        the configuration for data transformation.

        Returns:
            DataTransformationConfig: Configuration for data transformation.
        """
        data_transformation = self.config.data_transformation

        create_directories([data_transformation.root_dir])

        file_path = os.path.join(data_transformation.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {data_transformation.root_dir}"
                )
                pass

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(data_transformation.root_dir),
            unzip_data_path=Path(data_transformation.unzip_data_path),
            status_file_path=Path(data_transformation.status_file_path),
        )

        return data_transformation_config
