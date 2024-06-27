import re 
from datetime import datetime

class clean_data:
    def __init__(self,dictionary_list = None):
        self.dictionary_list = dictionary_list

        if dictionary_list is None:
            raise ValueError("'dictionary_list' cannot be found")
        
        if not isinstance(dictionary_list,list):
            raise TypeError("'dictionary_list' must be a list")
        
    def extract_info(selfm, option_string = None):
        pattern = r"([A-Z]+)(\d{2})([A-Z]{3})(\d{2})(\d+)(PE|CE)\.NFO"
        match = re.match(pattern,option_string)

        if match:
            stock_name = match.group(1)
            day = match.group(2)
            month = match.group(3)
            year = match.group(4)
            strike_price = match.group(5)
            option_type = match.group(6)

            expiry_date = datetime.strptime(f"{day} {month} {year}","%d %b %y").date().strftime("%d %b %Y")


            return {
                "STOCK_NAME": stock_name,
                "EXPIRY": expiry_date,
                "STRIKE": strike_price,
                "OPTION_TYPE": option_type
            }
        else:
            return None

    def clean_list_of_dicts(self):
        for d in self.dictionary_list:
            if 'Ticker' in d:
                extracted_info = self.extract_info(d['Ticker'])
                if extracted_info:
                    d.update(extracted_info)

    
        
    