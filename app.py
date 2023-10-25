import os

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

from mlflow_project.pipeline.prediction import PredictionPipeline
from mlflow_project import logger


app = Flask(__name__)  # initialize a flask app


@app.route("/", methods=["GET"])  # route to display the index/home page
def index():
    return render_template("index.html")


@app.route("/train", methods=["GET"])
def train():
    os.system("python main.py")

    return "Training Successful!"


@app.route(
    "/predict", methods=["GET", "POST"]
)  # route to show the predictions in a web UI
def predict():
    if request.method == "POST":
        try:
            # Read the inputs given by the user
            fixed_acidity = float(request.form["fixed_acidity"])
            volatile_acidity = float(request.form["volatile_acidity"])
            citric_acid = float(request.form["citric_acid"])
            residual_sugar = float(request.form["residual_sugar"])
            chlorides = float(request.form["chlorides"])
            free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
            total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
            density = float(request.form["density"])
            pH = float(request.form["pH"])
            sulphates = float(request.form["sulphates"])
            alcohol = float(request.form["alcohol"])

            data = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol,
            ]
            data = np.array(data).reshape(1, 11)

            prediction_pipeline = PredictionPipeline()
            pred = prediction_pipeline.predict(data)

            return render_template("results.html", prediction=str(pred))

        except Exception as e:
            logger.exception(e)

            return "Something went wrong!"

    else:
        return render_template("index.html")


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="0.0.0.0", port=8080)
