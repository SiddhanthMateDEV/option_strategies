import numpy as np 
import pandas as pd 
import sys
import os
import subprocess
from pymongo import MongoClient
from datetime import datetime
import time
from concurrent.futures import ProcessPoolExecutor

'''
Going the create a options trading algo and test it on the jpyter notebook on the left
'''

'''
Creating a class to clean data according to a pattern and store it in a database first 
'''

def start_mongodb(db_path):
    subprocess.Popen(['mongod','--dbpath',db_path])
    time.sleep(5)

def stop_mongodb():
    subprocess.Popen(['mongo','--eval','db.adminCommand({shutdown: 1})'])

def get_files(root_path = None):
    # Get a list of the file names in the root directory
    return [file_[:-4] for file_ in os.listdir(root_path) if file_.endswith(".csv")]

class database_creation:
    def __init__(self, 
                 db_path = None,
                 collection_name = None):
        # Global variables needed throughout
        self.db_path = db_path
        self.collection_name = collection_name
        self.file_attr = {}
    
    def extract_attributes_of_file(self):
        # for bookeeping purposes lets do some extra steps
        '''
        for example what were doing here is that i have files 
        in the form of this string path: "/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/DATA/options_data/2022/14112022.csv"
        i want the variables of day month and year as a string
        '''
        
        day = self.file[:2]
        month = self.file[2:4]
        year = self.file[4:]

        '''
        returning a dictionary of this will be more effecient i think if i am going to run this 
        in a multiprocess fashion 
        '''
        self.file_attr = {
            "day": day,
            "month": month,
            "year": year,
            "collectio_name": self.collection_name,
        }
    
    def insert_database(self, 
                        day = None, 
                        month = None,
                        year = None,
                        collection_name = None
                        ):
        
        data_obj = datetime.strptime(fr"{day}{month}{year}","%d%m%y")
        
        data_str = fr"{day}-{month}-{year}"
        db_name = fr"db_{data_str}"

        # read the csv data file
        df = pd.read_csv(fr"{self.file}")
        mongo_uri = "mongodb://localhost:5000/"
        client = MongoClient(mongo_uri)
        db = client[str(db_name)]
        collection = db[str(collection_name)]
        data_dict = df.to_dict("records")
        collection.insert_many(data_dict)
        print(fr"Data for the {db_name} Entered Succesfully")

    def create_database(self, 
                        file = None):
        start_mongodb(self.db_path)
        try:
            self.extract_attributes_of_file()
            self.insert_database(**self.file_attr)
        finally:
            stop_mongodb()


def main():
    root_dir = fr"/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/DATA/options_data/2022"
    files = get_files(root_path = root_dir)
    cpu_no_ = os.cpu_count()

    class_attr = {
        "collection_name": "options_data",
        "db_path": fr"/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/options_strategies/database" 
    }
    db_creator = database_creation(**class_attr)
    with ProcessPoolExecutor(max_workers = cpu_no_) as executor:
        executor.map(db_creator.create_database,files)

if __name__=="__main__":
    main()