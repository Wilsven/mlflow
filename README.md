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

## 1. Clone the Repository

```bash
git clone https://github.com/Wilsven/mlops-with-mlflow.git
```

## 2. Create a `conda` Environment

```bash
conda create -n <ENV NAME> python=3.11 -y
```

```bash
conda activate <ENV NAME>
```

## 3. Install the Requirements

```bash
pip install -r requirements.txt
```

## 4. Start the Application

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

# AWS CI/CD Deployment with Github Actions

## 👣 Steps

## 1. Login to AWS Console

## 2. Create IAM User for Deployment

    # Specific access

    1. EC2 access : It is a virtual machine

    2. ECR: Elastic Container registry to save your docker image in AWS


    # Description

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull your image from ECR in EC2

    5. Lauch your docker image in EC2

    # Policy

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR Repository to store/save Docker Image

    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

## 4. Create EC2 Machine (Ubuntu)

## 5. Open EC2 and Install Docker in EC2 Machine

    # Optional

    sudo apt-get update -y

    sudo apt-get upgrade -y

    # Required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## 6. Configure EC2 as Self-hosted Runner:

    Settings > Actions > Runner > New self-hosted runner > Select Linux > Execute commands one by one in your Virtual Machine

## 7. Setup GitHub Secrets

    AWS_ACCESS_KEY_ID

    AWS_SECRET_ACCESS_KEY

    AWS_REGION

    AWS_ECR_LOGIN_URI

    ECR_REPOSITORY_NAME

# About MLflow

- Production Grade
- Experiment tracking
- Loging
- Tagging
