import pandas as pd

from mlflow_project import logger
from mlflow_project.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validation_columns(self) -> bool:
        """Validates the data schema and data types.

        Raises:
            e: Exception.

        Returns:
            bool: False if validation failed else True.
        """
        try:
            validation_status = None

            df = pd.read_csv(self.config.unzip_data_path)
            columns_datatypes = df.dtypes.to_dict()
            data_schema = self.config.data_schema

            for col, dtype in columns_datatypes.items():
                # If column not in schema, validation failed
                if col not in data_schema:
                    validation_status = False
                    with open(self.config.status_file_path, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                    return validation_status
                # If column in schema, then proceed to check data type and if not the same, validation failed
                elif dtype != data_schema[col]:
                    validation_status = False
                    with open(self.config.status_file_path, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                    return validation_status

            # After everything, validation success
            validation_status = True
            with open(self.config.status_file_path, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.exception(e)
            raise e
