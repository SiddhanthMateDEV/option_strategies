import pandas as pd 
import numpy as np
import datetime as datetime
from equity_strategies import atr, dma

try:
    from trade_attributes import trade_attributes
except ImportError as e:
    print("Error: Could not import 'trade_attributes'")

class equity_strategies(trade_attributes,atr,dma):
    def __init__(self, 
                 sl = None, tsl = None, pb = None, init_cap = None,
                 n_slow_atr = None ,n_fast_atr = None,n_tma = None):
        trade_attributes.__init__(sl, tsl, pb, init_cap)
        atr.__init__(n_slow_atr,n_fast_atr,n_tma)
    


