import numpy as np 
import pandas as pd 
import sys
import os
import subprocess
from pymongo import MongoClient
from datetime import datetime
import time

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


class database_creation:
    def __init__(self, 
                 root_path = None,
                 db_path = None,
                 collection_name = None):
        # Global variables needed throughout
        self.root_path = root_path
        self.db_path = db_path
        self.collection_name = collection_name
    
    def get_files(self):
        # Get a list of the file names in the root directory
        return [file_[:-4] for file_ in os.listdir(self.root_path) if file_.endswith(".csv")]
    
    def extract_attributes_of_file(self, file = None):
        # for bookeeping purposes lets do some extra steps
        '''
        for example what were doing here is that i have files 
        in the form of this string path: "/Users/siddhanthmate/Desktop/AllFiles/CODE/WORK_CODE/fintech/DATA/options_data/2022/14112022.csv"
        what i want to do is i want to slice the basename since thats the datetime stamp 
        i want the variables of day month and year as a string
        '''
        
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
            "collectio_name": self.collection_name,
        }
    
    def insert_data_base(self, 
                        day = None, 
                        month = None,
                        year = None,
                        db_name = None,
                        collection_name = None
                        ):
        

        data_obj = datetime.strptime(fr"{day}{month}{year}","%d%m%y")
        
        data_str = fr"{day}-{month}-{year}"
        db_name = fr"db_{data_str}"

        # read the csv data file
        df = pd.read_csv(fr"{self.root_path}/{day}{month}{year}.csv")
        mongo_uri = "mongodb://localhost:5000/"
        client = MongoClient(mongo_uri)
        db = client[str(db_name)]
        collection = db[str(collection_name)]
        data_dict = df.to_dict("records")
        collection.insert_many(data_dict)
        print(fr"Data for the {db_name} Entered Succesfully")

    def 

