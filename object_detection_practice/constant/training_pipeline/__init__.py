import os

ARTIFACTS_DIR : str = 'artifacts'


"""
Data Ingestion related contants start with DATA_INGESTION_VAR_NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR_NAME : str= "feature_store"

DATA_DOWNLOAD_URL:str = "https://github.com/Hasnain-Khattak/Object-Detection-project/raw/refs/heads/main/Dataset.zip"


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]



"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16

MODEL_TRAINER_IMAGE_SIZE: int = 640
