
from datetime import datetime
import os
from this import d
from tkinter import Y

ROOT_DIR= os.getcwd()   # to get current working directory

CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"


#training pipeline related variable

TRAINING_PIPELINE_CONFIG_KEY="trianing_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY="artifact_dir"
TRAINING_PIPELINE_NAME_KEY="pipeline_name"