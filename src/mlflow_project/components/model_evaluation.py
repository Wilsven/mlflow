import os
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import mlflow
import mlflow.sklearn
from mlflow_project.entity.config_entity import ModelEvaluationConfig
from mlflow_project.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(
        self,
        actual: Union[np.ndarray, pd.DataFrame],
        pred: Union[np.ndarray, pd.DataFrame],
    ) -> tuple[float]:
        """Calculates evaluation metrics.

        Args:
            actual (Union[np.ndarray, pd.DataFrame]): Actual results.
            pred (Union[np.ndarray, pd.DataFrame]): Predicted results.

        Returns:
            tuple(float): The evaluation metrics (i.e. RMSE, MAE and R2) as a tuple of floats.
        """
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2

    def log_into_mlflow(self) -> None:
        """MLFlow for experiment tracking."""
        # Load the test set
        test_data = pd.read_csv(self.config.test_data_path)
        # Split the test set into independent and dependent features
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Load the pre-trained model
        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            # Predictions
            pred_y = model.predict(test_x)
            # Evaluate metrics
            rmse, mae, r2 = self.eval_metrics(test_y, pred_y)

            # Check if metrics.json exists, delete it
            if os.path.exists(self.config.metrics_file_path):
                os.remove(self.config.metrics_file_path)

            # Saving metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=self.config.metrics_file_path, data=scores)

            params = {
                "alpha": self.config.alpha,
                "l1_ratio": self.config.l1_ratio,
                "random_state": self.config.random_state,
            }
            # Log hyperparameters
            mlflow.log_params(params)

            # Log metrics
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # Please refer to the documentation for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="ElasticNetModel"
                )
            else:
                mlflow.sklearn.log_model(model, "model")
