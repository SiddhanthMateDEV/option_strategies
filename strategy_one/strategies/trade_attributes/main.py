try:
    from validate_variables.main import validator
except Exception as e:
    raise ImportError(fr"Error: Could not import 'validator")

"""
The attributed of 'trade_attributes' class are:

sl = Stop Loss
tsl = Trailing Stop Loss
pb = Profit Booking
cp = Cost of each Trade in %
stock = Stock Name
start_time = Starting Trade time


Here a tick is a unit of the timeframe:
new_tick = New Day Tick Number, typically 1 or 0
eod_tick = End of day tick is depends on the timeframe
"""

class trade_attributes(validator):
    def __init__(self,
                 sl = None,
                 tsl = None,
                 pb = None,
                 init_cap = None,
                 cp = None,
                 stock = None,
                 start_time = None,
                 new_tick = None,
                 eod_tick = None,
                 ):
        
        self.sl = sl
        self.stock = stock
        self.tsl = tsl
        self.pb = pb
        self.cp = cp
        self.init_cap = init_cap
        self.start_time = start_time
        self.new_tick = new_tick
        self.eod_tick = eod_tick
        self.validate()

    def display_attr(self):
        if (self.sl and self.tsl and self.pb and self.initial_capital):
            print(f"Stock Name: {self.stock}")
            print(f"Stop Loss: {self.sl}")
            print(f"Trailing Stop Loss: {self.tsl}")
            print(f"Profit Booking: {self.pb}")
            print(f"Cost Percentage: {self.cp}")
            print(f"Initial Capital: {self.init_cap}")
            print(f"No. Of Days of Trading: {self.t_days}")

