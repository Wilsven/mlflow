import os

import pandas as pd
from sklearn.model_selection import train_test_split

from mlflow_project import logger
from mlflow_project.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # Different data transformation techniques such can be applied
    # Differrent kinds of EDA in the ML cycle can be performed here before passing the data to the model
    # Only `train_test_split` will be used here because this is a project focusing on MLOps
    def train_test_split(self) -> None:
        """Splits the data into train and test sets."""
        df = pd.read_csv(self.config.unzip_data_path)

        # Split the data into train and test sets -> 3 to 1 split
        train, test = train_test_split(df, train_size=0.75)
        logger.info("Successfully split data into train and test sets")

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Successfully saved the train set with shape: {train.shape}")
        logger.info(f"Successfully saved the test set with shape: {test.shape}")
