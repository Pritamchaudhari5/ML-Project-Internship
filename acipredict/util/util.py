import sys
import yaml

from acipredict.exception import ACIPredictionException
import os,sys




def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ACIPredictionException(e,sys) from e 