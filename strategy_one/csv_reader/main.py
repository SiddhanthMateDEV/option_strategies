import pandas as pd

class csv_reader:
    def __init__(self,file = None):
        if file is None:
            raise ValueError("'file' is empty")
        
        self.file = file
        self.df = self._reader()
        self.data_dictionary = self._create_data_dictionary()


    def _reader(self):
        return pd.read_csv(self.file)

    def _create_data_dictionary(self):
        return self.df.to_dict("records")

    def get_data_dict(self):
        return self.data_dictionary        

