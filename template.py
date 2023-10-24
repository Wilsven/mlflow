import logging
import os
from datetime import datetime
from pathlib import Path

LOGS_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)


os.makedirs(LOGS_DIR, exist_ok=True)

if not os.path.exists(os.path.join(LOGS_DIR, ".gitkeep")):
    with open(os.path.join(LOGS_DIR, ".gitkeep"), "w") as f:
        pass

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(module)s %(name)s -  %(levelname)s - %(message)s",
)

PROJECT_NAME = "mlflow_project"

FILE_PATHS = [
    ".github/workflows/.gitkeep",
    "Dockerfile",
    "app.py",
    "config/config.yaml",
    "main.py",
    "params.yaml",
    "requirements.txt",
    "research/trials.ipynb",
    "schema.yaml",
    "setup.py",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    "templates/index.html",
]

for file_path in FILE_PATHS:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if len(file_dir) != 0:
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}")

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            logging.info(f"Creating file: {file_name}")
            pass

    else:
        logging.info(
            f"File {file_name} already exists in file directory/path {file_dir}"
        )
