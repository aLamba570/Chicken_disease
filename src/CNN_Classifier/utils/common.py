import os
import yaml
import json
import joblib
from box.exceptions import BoxValueError
from CNN_Classifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories.
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {directory}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary to a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return a ConfigBox object.
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save a binary file.
    """
    data = joblib.dump(data)
    with open(path, "wb") as f:
        f.write(data)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load a binary file and return the data.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data 


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file.
    """ 
    size_in_kb = round(os.path.getsize(path)/1024)  
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()
    logger.info(f"file saved at: {filename}")

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read())
        
