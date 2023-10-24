from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_path: Path
    status_file_path: Path
    data_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    unzip_data_path: Path
