"""
The attributed of 'trade_attributes' class are:

sl = Stop Loss
tsl = Trailing Stop Loss
pb = Profit Booking
cp = Cost of each Trade in %
"""

class trade_attributes:
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

    def display_attr(self):
        if (self.sl and self.tsl and self.pb and self.initial_capital):
            print(f"Stock Name: {self.stock}")
            print(f"Stop Loss: {self.sl}")
            print(f"Trailing Stop Loss: {self.tsl}")
            print(f"Profit Booking: {self.pb}")
            print(f"Cost Percentage: {self.cp}")
            print(f"Initial Capital: {self.init_cap}")
            print(f"No. Of Days of Trading: {self.t_days}")

    # def _validate()