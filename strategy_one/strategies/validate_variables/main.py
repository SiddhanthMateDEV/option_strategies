import logging
import threading
from datetime import datetime


logging.basicConfig(
    filename='class_logging.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_usage(class_name = None, variable = None, value = None):
    logging.info(f"Class Name: {class_name} | Variable Name: {variable} | Value: {value}")

class validator:
    def __init__(self,
                 **kwargs):
        self.attributes = kwargs

    def validate(self):
        for key, val in self.attributes.items():
            if val is None:
                raise ValueError(f"The value of '{key}' cannot be set to None")
            log_usage(class_name = self.__class__.__name__, variable = key, value = val)

