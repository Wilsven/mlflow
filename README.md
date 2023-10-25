# MLOps with MLFlow

# 📋 Workflows

1. Update `config.yaml`
2. Update `schema.yaml` _[For validation]_
3. Update `params.yaml` _[For training]_
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline
8. Update the `main.py`
9. Update the `app.py`

# 🤷🏻‍♂️ How to run?

## 👣 Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Wilsven/mlops-with-mlflow.git
```

### 2. Create a `conda` Environment

```bash
conda create -n <ENV NAME> python=3.11 -y
```

```bash
conda activate <ENV NAME>
```

### 3. Install the Requirements

```bash
pip install -r requirements.txt
```

### 4. Start the Application

```bash
python app.py
```

# 🌊 [MLflow](https://mlflow.org/docs/latest/index.html)

# 🐶 [Dagshub](https://dagshub.com/)

```
MLFLOW_TRACKING_URI=https://dagshub.com/Wilsven/mlops-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=Wilsven \
MLFLOW_TRACKING_PASSWORD=your_token \
python script.py
```

Run the following commands to export as environment variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/Wilsven/mlops-with-mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=Wilsven

export MLFLOW_TRACKING_PASSWORD=your_token
```

Or you can create an `.env` file in the root directory:

```env
MLFLOW_TRACKING_URI=https://dagshub.com/Wilsven/mlops-with-mlflow.mlflow
MLFLOW_TRACKING_USERNAME=Wilsven
MLFLOW_TRACKING_PASSWORD=your_token
```

Edit the `.env.example` file and rename it to `env` when done.
