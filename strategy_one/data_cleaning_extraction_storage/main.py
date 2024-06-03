import numpy as np 
import pandas as pd 
import sys
import os
import subprocess
from pymongo import MongoClient
from datetime import datetime
import time
from concurrent.futures import ProcessPoolExecutor
import logging

logging.basicConfig(filename='database_creation.log', 
                    level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')

def start_mongodb(db_path):
    subprocess.Popen(['mongod','--dbpath',db_path])
    time.sleep(5)

def stop_mongodb():
    subprocess.Popen(['mongo','--eval','db.adminCommand({shutdown: 1})'])

def get_files(root_path):
    # Get a list of the file names in the root directory
    if root_path is None:
        raise ValueError("root_path is not specified")
    return [file_[:-4] for file_ in os.listdir(root_path) if file_.endswith(".csv")]


def extract_attributes_of_file(file):
    # for bookeeping purposes lets do some extra steps
    '''
    for example what were doing here is that i have files 
    in the form of this string path: "/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/DATA/options_data/2022/14112022.csv"
    i want the variables of day month and year as a string
    '''
    if file is None:
        raise ValueError("File and collection_name must be specified")
    

    day = file[:2]
    month = file[2:4]
    year = file[4:]

    '''
    returning a dictionary of this will be more effecient i think if i am going to run this 
    in a multiprocess fashion 
    '''
    return {
        "day": day,
        "month": month,
        "year": year,
        "file": file
    }
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
        self.file_attr = {}
        self.client = MongoClient("mongodb://localhost:27017/")
        logging.info(f"Initialised database_creation with db_path")
    
    def insert_database(self, 
                        day = None, 
                        month = None,
                        year = None,
                        file = None
                        ):
        
        data_obj = datetime.strptime(fr"{day}{month}{year}","%d%m%y")
        
        data_str = fr"{day}-{month}-{year}"
        db_name = fr"db_{data_str}"

        # read the csv data file
        df = pd.read_csv(fr"{self.root_path}/{file}.csv")
        mongo_uri = "mongodb://localhost:5000/"
        client = MongoClient(mongo_uri)
        db = client[str(db_name)]
        collection = db[str(self.collection_name)]
        data_dict = df.to_dict("records")
        collection.insert_many(data_dict)
        logging.info(f"Data entered: {db_name}")
        print(fr"Data for the {db_name} Entered Succesfully")


    def create_database(self, 
                        file):
        
        try:
            file_attr_dictionary = extract_attributes_of_file(file)
            self.insert_database(**file_attr_dictionary)
        except Exception as e:
            logging.info(f"Error Creating database for file {file}: {e}")

def main():
    root_dir = fr"/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/DATA/options_data/2022"
    file = get_files(root_path = root_dir)

    # here im putting the upper limit of cpu usage adjust this accordingly
    cpu_no_ = os.cpu_count()

    class_attr = {
        "collection_name": "options_data",
        "db_path": fr"/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/options_strategies/database",
        "root_path": root_dir
    }

    # pre initialise the class 
    db_creator = database_creation(**class_attr)

    try:
        with ProcessPoolExecutor(max_workers = cpu_no_) as executor:
            executor.map(db_creator.create_database,file)
    except Exception as e:
        logging.error(f"Error in ProcessPoolExecutor: {e}")

if __name__=="__main__":
    main()