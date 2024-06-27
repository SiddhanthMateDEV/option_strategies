import numpy as np 
import pandas as pd 
import sys
import os
import subprocess
from pymongo import MongoClient
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor
import logging


def debug(func):
    def wrapper():
        function_name = func.__name__
        message = fr"{function_name} Running"
        return message
    return wrapper

logging.basicConfig(filename='database_creation.log', 
                    level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')

def start_mongodb(db_path):
    try:
        subprocess.Popen(['mongod','--dbpath',db_path])
        time.sleep(5)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error starting MongoDB: {e}")

def stop_mongodb():
    try:
        subprocess.Popen(['mongosh','--eval','db.getSiblingDB("admin").shutdownServer()'])
    except subprocess.CalledProcessError as e:
        logging.error(f"Error stopping MongoDB: {e}")

def get_files(root_path):
    # Get a list of the file names in the root directory
    if root_path is None:
        raise ValueError("root_path is not specified")
    return [file_[:-4] for file_ in os.listdir(root_path) if file_.endswith(".csv")]

class database_creation:
    def __init__(self, 
                 db_path = None,
                 collection_name = None,
                 root_path = None
                 ):
        # Global variables needed throughout
        if db_path is None or collection_name is None:
            raise ValueError("db_path and collection_name must be specified")
        
        self.root_path = root_path
        self.db_path = db_path
        self.collection_name = collection_name
        self.file = None
        self.day = None
        self.month = None
        self.year = None
        self.file_attr = {}
        self.client = MongoClient("mongodb://localhost:27017/")
        logging.info(f"Initialised database_creation with db_path")

    @debug
    def extract_attributes_of_file(self,file):
        # for bookeeping purposes lets do some extra steps
        '''
        for example what were doing here is that i have files 
        in the form of this string path: "/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/DATA/options_data/2022/14112022.csv"
        i want the variables of day month and year as a string
        '''
        if file is None:
            raise ValueError("File and collection_name must be specified")
        
        self.file = file
        self.day = self.file[:2]
        self.month = self.file[2:4]
        self.year = self.file[4:]

    @debug
    def insert_database(self):
                
        data_str = fr"{self.day}_{self.month}_{self.year}"
        db_name = fr"db_{data_str}"

        df = pd.read_csv(fr"{self.root_path}/{self.file}.csv")
        
        with self.client:
            db = self.client[str(db_name)]
            collection = db[str(self.collection_name)]
            data_dict = df.to_dict("records")
            result = collection.insert_many(data_dict)

        logging.info(f"Data entered: {db_name}")
        print(fr"Data for the {db_name} Entered Succesfully")

    @debug
    def create_database(self,file = None):
        
        try:
            self.extract_attributes_of_file(file = file)
            logging.debug("Attributes of the file are extracted")
            self.insert_database()
            logging.info("Database inserted into the collection")
        except Exception as e:
            logging.error(f"Error Creating database for file {self.file}: {e}")

    # @debug
    # def file_last_call(self):
    #     print(fr"{db_name}")


def thread_function(collection_name = None,
                    db_path = None,
                    root_path = None,
                    files_ = None
                    ):
    class_attr = {
        "collection_name": collection_name,
        "db_path": db_path,
        "root_path": root_path
    }

    cpu_no_ = os.cpu_count()
    try:
        with ThreadPoolExecutor(max_workers = cpu_no_) as executor:
            db_creator = database_creation(**class_attr)
            executor.map(db_creator.create_database,files_)
    except Exception as e:
        logging.error(f"Error in ThreadPoolExecutor: {e}")


def main():
    root_dir = fr"/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/DATA/options_data/2022"


    parent_filename_1 = fr"/Users/siddhanthmate/Desktop/AllFiles/DATA/options_data/drive-download-20240512T050709Z-006"

    root_dir = [
                fr"{parent_filename_1}/2022",
                fr"{parent_filename_1}/NIFTY",
                fr"{parent_filename_1}/SET1DATA"
    ]

    files_ = get_files(root_path = root_dir)
    # here im putting the upper limit of cpu usage adjust this accordingly
    cpu_no_ = os.cpu_count()
    class_attr = {
        "collection_name": "options_data",
        "db_path": fr"/usr/local/var/mongodb",
        "root_path": root_dir
    }
    # start_mongodb(class_attr["db_path"])
    cpu_no_ = os.cpu_count()
    
    try:
        with ThreadPoolExecutor(max_workers = cpu_no_) as executor:
            db_creator = database_creation(**class_attr)
            executor.map(db_creator.create_database,files_)
    except Exception as e:
        logging.error(f"Error in ThreadPoolExecutor: {e}")
    
if __name__=="__main__":
    main()