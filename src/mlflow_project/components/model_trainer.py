import os

import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet

from mlflow_project.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self) -> None:
        """Trains the model."""
        train_data = pd.read_csv(self.config.train_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]

        elastic_net = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=self.config.random_state,
        )
        elastic_net.fit(train_x, train_y)

        joblib.dump(
            elastic_net, os.path.join(self.config.root_dir, self.config.model_name)
        )
