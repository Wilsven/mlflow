from pathlib import Path
from typing import Union

import joblib
import numpy as np
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def predict(self, data: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """Predicts the output for a given input data.

        Args:
            data (Union[np.ndarray, pd.DataFrame]): Input data.

        Returns:
            np.ndarray: Output prediction.
        """
        pred = self.model.predict(data)

        return pred
